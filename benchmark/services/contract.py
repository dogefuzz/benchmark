import csv
import os

from benchmark.config import Config
from benchmark.shared.exceptions import ContractsNotFoundException

NAME_COLUMN = 0
VULNERABILITIES_COLUMN = 1
LINK_COLUMN = 2


class ContractService():
    """sertice that contains operations with the available contracts
    """

    def __init__(self) -> None:
        self._config = Config()

    def list_contracts_from_contract_folder(self) -> list:
        """lists the contracts from the contracts/ folder
        """
        if not os.path.exists(self._config.contracts_folder):
            raise ContractsNotFoundException(
                "the contracts were not downloaded yet. Please use the command download_contracts first")

        contracts = []
        contracts_dir = os.path.join(
            self._config.contracts_folder, "contracts")
        for file in os.listdir(contracts_dir):
            if os.path.isfile(os.path.join(contracts_dir, file)):
                contracts.append(file)

        return contracts

    def list_contracts_from_contract_list(self) -> list:
        """lists the contracts from the contracts.csv file
        """
        if not os.path.exists(self._config.contracts_folder):
            raise ContractsNotFoundException(
                "the contracts were not downloaded yet. Please use the command download_contracts first")

        contracts = []
        contracts_csv = os.path.join(
            self._config.contracts_folder, "contracts.csv")
        with open(contracts_csv, 'r', encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                contract = {
                    "name": row[NAME_COLUMN],
                    "vulnerabilities": row[VULNERABILITIES_COLUMN].split(";"),
                    "link": row[LINK_COLUMN],
                }
                contracts.append(contract)

        return contracts
