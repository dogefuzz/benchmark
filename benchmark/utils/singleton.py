"""
this module contains metaclasses used in other parts of the project
reference: https://refactoring.guru/design-patterns/singleton/python/example#example-1
"""
from threading import Lock
from typing import Any


class SingletonMeta(type):
    """
    this class contains the implementation of the singleton pattern
    """
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwds)
                cls._instances[cls] = instance
        return cls._instances[cls]
