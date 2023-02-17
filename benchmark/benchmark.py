"""
Cli moodule
"""


from time import sleep
from benchmark.services.contract import ContractService
from benchmark.services.dogefuzz import DogefuzzService
from benchmark.services.progress import ProgressService
from benchmark.services.queue import QueueService
from benchmark.services.server import ServerService
from benchmark.services.drive import DriveService
from benchmark.shared.time import parse_timedelta


class Benchmark():
    """
    the CLI options for benchmarking the Dogefuzz project
    """

    def __init__(self) -> None:
        self._dogefuzz_service = DogefuzzService()
        self._progress_service = ProgressService()
        self._server_service = ServerService()
        self._queue = QueueService()
        self._drive_service = DriveService()
        self._contract_service = ContractService()

    def single(self, contract: str, duration: str, fuzzing_type: str, args: str = ""):
        """
        benchmark single contracts
        """
        self._server_service.start()

        duration_delta = parse_timedelta(duration)
        self._dogefuzz_service.test_single_contract(
            contract, args, duration, fuzzing_type)
        self._progress_service.start()

        step_percentage = 25
        for idx in range(duration_delta.seconds):
            sleep(1)
            self._progress_service.update_progress_bar(
                step_percentage, idx + 1)
        self._progress_service.stop()

    def batch(self, contracts: list, duration: str, fuzzing_type: str):
        """
        benchmark multiple contracts
        """
        print(
            f"contracts = {contracts}, duration = {duration}, fuzzing_type={fuzzing_type}")

    def all(self, duration: str, fuzzing_type: str):
        """
        benchmark all available contracts
        """
        print(f"duration = {duration}, fuzzing_type={fuzzing_type}")

    def download_contracts(self):
        """
        download contracts from cloud
        """
        self._drive_service.download_contracts()

    def list_available_contracts(self):
        """
        list available contracts
        """
        contracts = self._contract_service.list_contracts_from_contract_list()
        print(f"read {len(contracts)} contracts:")
        # print("\n".join(contracts))
        for element in contracts:
            print(element)
