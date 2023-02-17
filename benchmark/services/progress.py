"""
"""
from queue import Queue
from tqdm import tqdm
from benchmark.shared.singleton import SingletonMeta


class ProgressService(metaclass=SingletonMeta):
    """
    the service that shows the current progress of the benchmark
    """

    def __init__(self) -> None:
        self._progress_bar: tqdm = None
        self._queue = Queue()

    def start(self):
        """
        start progress bar in CLI
        """
        self._progress_bar = tqdm(total=100, desc="Progress")

    def update_progress_bar(self, percentage: float):
        """
        update progress bar passing the amount of values
        """
        self._progress_bar.update(percentage)

    def update_transaction_count(self, transactions_count: int) -> None:
        """
        update transaction ocunt
        """
        self._progress_bar.set_postfix_str(
            f"transactions: {transactions_count}")

    def stop(self):
        """
        stop the progress bar
        """
        self._progress_bar.close()
