"""CLI moodule
"""
import json
import multiprocessing
import signal
import os

from datetime import datetime
from benchmark.services.contract import ContractService
from benchmark.services.benchmark import BenchmarkService
from benchmark.services.progress import ProgressService
from benchmark.services.drive import DriveService
from benchmark.services.script import ScriptService
from benchmark.shared.testing import RequestFactory

stop_threads = multiprocessing.Event()


def signal_handler(sig, frame):
    print('You pressed Ctrl+C! shuting down benchmark...')
    stop_threads.set()


signal.signal(signal.SIGINT, signal_handler)


class Benchmark():
    """the CLI options for benchmarking the Dogefuzz project
    """

    def __init__(self) -> None:
        self._benchmark_service = BenchmarkService()
        self._progress_service = ProgressService()
        self._drive_service = DriveService()
        self._contract_service = ContractService()
        self._script_service = ScriptService()

    def script(self):
        """benchmarks based on a script file
        """
        request = self._script_service.read_testing_request_from_script()
        result = self._benchmark_service.run(request, stop_threads)
        self._write_result(result)

    def all(self, duration: str, fuzzing_types: str, times: str):
        """benchmarks all available contracts
        """
        fuzzing_types_list = fuzzing_types.split(",")
        contracts = self._contract_service.list_contracts_from_contract_list()
        request = RequestFactory.from_contracts_list(
            contracts, duration, fuzzing_types_list, times)

        result = self._benchmark_service.run(request, stop_threads)
        self._write_result(result)
        print("SUCCESS")

    def generate_results(self, timestamp: str):
        """generates the results
        """
        self._progress_service.generate_results()

    def download_contracts(self):
        """downloads contracts from cloud
        """
        self._drive_service.download_contracts()

    def list_available_contracts(self):
        """lists available contracts
        """
        contracts = self._contract_service.list_contracts_from_contract_list()
        print(f"read {len(contracts)} contracts:")
        for element in contracts:
            print(element)

    def _write_result(self, result: list):
        """writes the result to a file
        """
        timestamp = datetime.now().timestamp()
        folder_path = os.path.join("results", str(timestamp))
        os.makedirs(folder_path, exist_ok=True)

        with open(f"{folder_path}/result.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(result, indent=4))
