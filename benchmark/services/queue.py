"""
"""
from queue import Empty
from multiprocessing import Queue
from benchmark.shared.dogefuzz.api import TaskReport
from benchmark.shared.singleton import SingletonMeta


class QueueService(metaclass=SingletonMeta):

    def __init__(self) -> None:
        self._queue = Queue()

    def put(self, report: TaskReport) -> None:
        """puts report in the queue
        """
        self._queue.put(report)

    def is_empty(self) -> bool:
        """checks if queue is empty
        """
        return self._queue.empty()

    def get(self) -> TaskReport:
        """gets report from the queue
        """
        value = None
        try:
            value = self._queue.get_nowait()
        except Empty:
            return None
        return value
