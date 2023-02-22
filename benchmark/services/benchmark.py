"""
this module contains the service that communicate with dogefuzz
"""
from benchmark.services.contract import ContractService
from benchmark.services.dogefuzz import DogefuzzService
from benchmark.services.progress import ProgressService
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
        self._queue_service = ProgressService()
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
            task_id = self._dogefuzz_service.create_task(
                entry, contract_source)
            print(f"the task ${task_id} has started")
            result = self._wait_dogefuzz_respond()
            benchmark_result.append(result)
            step = 100/len(request.entries)
            self._progress_service.update_progress_bar(step)

        self._progress_service.stop()
        self._server_service.stop()

        return benchmark_result

    def _wait_dogefuzz_respond(self) -> TaskReport:
        report = None
        while True:
            task_report = self._dogefuzz_service.get()
            if task_report is not None:
                self._dogefuzz_service.mark_done()
                report = task_report
                break
        return report
