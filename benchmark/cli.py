"""
Cli moodule
"""


class Benchmark():
    """
    the CLI options for benchmarking the Dogefuzz project
    """

    def single(self, contract: str, args: list, duration: str, fuzzing_type: str):
        """
        benchmark single contracts
        """
        print(
            f"contract = {contract}, args = {args}, duration = {duration}, fuzzing_type={fuzzing_type}")

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

    def visualize_result(self, timestamp):
        """
        visualize results from timestamp
        """
        print(f"timestamp={timestamp}")
