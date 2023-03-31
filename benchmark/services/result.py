"""
this module contains the service the computes the result
"""
from benchmark.services.contract import ContractService
from benchmark.shared.singleton import SingletonMeta

class ResultService(metaclass=SingletonMeta):
    """this class represents the service the computes the result
    """

    def __init__(self) -> None:
        self._contract_service = ContractService()
