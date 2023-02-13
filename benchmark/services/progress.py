"""
"""
from tqdm import tqdm
from benchmark.utils.singleton import SingletonMeta


class ProgressService(metaclass=SingletonMeta):
    """
    the service that shows the current progress of the benchmark
    """

    def __init__(self) -> None:
        self._progress_bar: tqdm = None

    def start(self):
        """
        Start progress bar in CLI
        """
        self._progress_bar = tqdm(total=100, desc="Progress")

    def update_progress_bar(self, percentage: float, transactions_count: int):
        """
        Update progress bar passing the amount of values
        """
        self._progress_bar.update(percentage)
        self._progress_bar.set_postfix_str(
            f"transactions: {transactions_count}")

    def stop(self):
        """
        Stop the progress bar
        """
        self._progress_bar.close()
