"""
this module contains the service that communicate with dogefuzz
"""
from benchmark.shared.singleton import SingletonMeta
from benchmark.shared.testing import Request


class DogefuzzService(metaclass=SingletonMeta):

    def test_request(self, request: Request):
        pass
