"""
Cli moodule
"""


from time import sleep
from benchmark.services.dogefuzz import DogefuzzService
from benchmark.services.progress import ProgressService
from benchmark.utils.time import parse_timedelta


class Benchmark():
    """
    the CLI options for benchmarking the Dogefuzz project
    """

    def __init__(self) -> None:
        self._dogefuzz_service = DogefuzzService()
        self._progress_service = ProgressService()

    def single(self, contract: str, duration: str, fuzzing_type: str, args: str = ""):
        """
        benchmark single contracts
        """
        duration_delta = parse_timedelta(duration)
        self._dogefuzz_service.test_single_contract(
            contract, args, duration, fuzzing_type)
        self._progress_service.start()

        step_percentage = 100/duration_delta.seconds
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

    def download_contracts(self, url: str):
        """
        download contracts from cloud
        """
        print(f"url={url}")

    def list_contracts(self):
        """
        list available contracts
        """
        pass
