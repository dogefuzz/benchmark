"""CLI moodule
"""
import json
import multiprocessing
import signal

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
        with open("result.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(result, indent=4))
        print("SUCCESS")

    def all(self, duration: str, fuzzing_types: str, times: str):
        """benchmarks all available contracts
        """
        fuzzing_types_list = fuzzing_types.split(",")
        contracts = self._contract_service.list_contracts_from_contract_list()
        request = RequestFactory.from_contracts_list(
            contracts, duration, fuzzing_types_list, times)

        result = self._benchmark_service.run(request, stop_threads)
        with open("result.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(result, indent=4))
        print("SUCCESS")

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

