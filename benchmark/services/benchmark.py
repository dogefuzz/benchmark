"""
this module contains the service that communicate with dogefuzz
"""
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

    def run(self, request: Request) -> list:
        "runs the benchmark following the testing request class"
        self._server_service.start()
        self._progress_service.start()

        benchmark_result = []
        for entry in request.entries:
            contract_source = self._contract_service.read_contract(
                entry.contract)
            self._dogefuzz_service.start_task(entry, contract_source)
            # print(f"the task {task_id} has started")
            result = self._wait_dogefuzz_respond(
                timeout=int(entry.duration[:-1]))
            # print(f"the task {task_id} has finished")
            if result is None:
                benchmark_result.append({})
            else:
                benchmark_result.append(result.to_dict())
            step = 100/len(request.entries)
            self._progress_service.update_progress_bar(step)

        self._progress_service.stop()
        self._server_service.stop()

        return benchmark_result

    def _wait_dogefuzz_respond(self, timeout: int) -> TaskReport:
        report = None
        limit = (timeout + 5) * 60  # duration + 5 minutes
        time = 0
        while True:
            report = self._queue_service.get()
            if report is not None:
                break
            sleep(5)
            time = time + 5
            if time > limit:
                return None
        return report
