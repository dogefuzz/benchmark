"""
"""
from queue import Queue
from benchmark.utils.singleton import SingletonMeta


class QueueService(metaclass=SingletonMeta):

    def __init__(self) -> None:
        self._queue = Queue()

    def put(self, item: any) -> None:
        self._queue.put(item)

    def is_empty(self) -> bool:
        return self._queue.empty()

    def get(self) -> any:
        return self._queue.get()

    def mark_done(self) -> bool:
        return self._queue.task_done()
