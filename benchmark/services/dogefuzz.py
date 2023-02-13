"""
this module contains the service that communicate with dogefuzz
"""
from benchmark.utils.singleton import SingletonMeta


class DogefuzzService(metaclass=SingletonMeta):

    def test_single_contract(self, contract: str, args: list, duration: str, fuzzing_type: str):
        pass
