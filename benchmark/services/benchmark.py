"""
this module contains the service that peforms operations in the benchmark
"""
import multiprocessing

from time import sleep
from benchmark.services.contract import ContractService
from benchmark.services.dogefuzz import DogefuzzService
from benchmark.services.progress import ProgressService
from benchmark.services.queue import QueueService
from benchmark.services.server import ServerService
from benchmark.shared.dogefuzz.api import TaskReport
from benchmark.shared.singleton import SingletonMeta
from benchmark.shared.testing import Request


class BenchmarkService(metaclass=SingletonMeta):
    """this class represents the service that peforms operations in the benchmark
    """

    def __init__(self) -> None:
        self._server_service = ServerService()
        self._progress_service = ProgressService()
        self._queue_service = QueueService()
        self._dogefuzz_service = DogefuzzService()
        self._contract_service = ContractService()

    def run(self, request: Request, stop: multiprocessing.Event) -> list:
        "runs the benchmark following the testing request class"
        self._server_service.start()
        self._progress_service.start()

        executions = {}
        for entry in request.entries:
            if stop.is_set():
                break

            executions[entry.contract] = {}
            for fuzzing_type in entry.fuzzing_types:
                contract_executions = []
                for _ in range(entry.times):

                    contract_source = self._contract_service.read_contract(
                        entry.contract)
                    try:
                        self._dogefuzz_service.start_task(entry, contract_source, fuzzing_type)
                    except Exception:
                        contract_executions.append({})
                        step = 100/(len(request.entries)*len(entry.fuzzing_types)*entry.times)
                        self._progress_service.update_progress_bar(step)
                        continue

                    timeout = int(entry.duration[:-1])
                    result = self._wait_dogefuzz_respond(timeout, stop)
                    if result is None:
                        contract_executions.append({})
                    else:
                        contract_executions.append(result.to_dict())
                    step = 100/(len(request.entries)*len(entry.fuzzing_types)*entry.times)
                    self._progress_service.update_progress_bar(step)
                executions[entry.contract][fuzzing_type] = contract_executions

        self._progress_service.stop()
        self._server_service.stop()

        return executions

    def _wait_dogefuzz_respond(self, timeout: int, stop: multiprocessing.Event) -> TaskReport:
        report = None
        limit = (timeout + 5) * 60  # duration + 5 minutes
        time = 0
        while True:
            if stop.is_set():
                break

            report = self._queue_service.get()
            if report is not None:
                break
            sleep(5)
            time = time + 5
            if time > limit:
                return None
        return report
