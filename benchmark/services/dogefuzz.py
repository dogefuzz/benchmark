"""
this module contains the service that communicate with dogefuzz
"""
from os.path import splitext

from benchmark.config import Config
from benchmark.shared.dogefuzz.api import StartTaskRequest
from benchmark.shared.dogefuzz.client import DogefuzzClient
from benchmark.shared.singleton import SingletonMeta
from benchmark.shared.testing import Entry


class DogefuzzService(metaclass=SingletonMeta):
    """this class represents the service that performs operations with dogefuzz
    """

    def __init__(self) -> None:
        self._config = Config()
        self._client = DogefuzzClient(
            self._config.dogefuzz_endpoint, self._config.dogefuzz_timeout)

    def start_task(self, testing_entry: Entry, contract_source: str) -> str:
        """creates a task in dogefuzz service
        """
        filename_without_extension = splitext(testing_entry.contract)[0]
        request = StartTaskRequest(
            contract_source=contract_source,
            contract_name=filename_without_extension,
            arguments=testing_entry.args,
            duration=testing_entry.duration,
            fuzzing_type=testing_entry.fuzzing_type,
            detectors=self._config.detectors,
        )
        response = self._client.start_task(request)
        return response.task_id
