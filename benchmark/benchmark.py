"""CLI moodule
"""


from benchmark.services.contract import ContractService
from benchmark.services.benchmark import BenchmarkService
from benchmark.services.progress import ProgressService
from benchmark.services.drive import DriveService
from benchmark.services.script import ScriptService
from benchmark.shared.testing import RequestFactory
from benchmark.shared.utils import validate_duration, validate_fuzzing_type


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
        result = self._benchmark_service.run(request)
        print(result)

    def all(self, duration: str, fuzzing_type: str):
        """benchmarks all available contracts
        """
        validate_duration(duration)
        validate_fuzzing_type(fuzzing_type)

        contracts = self._contract_service.list_contracts_from_contract_list()
        request = RequestFactory.from_contracts_list(
            contracts, duration, fuzzing_type)

        result = self._benchmark_service.run(request)
        print(result)

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
