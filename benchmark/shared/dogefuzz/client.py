"""
this module contains logic of the client to the dogefuzz api
"""
import requests

from benchmark.shared.dogefuzz.api import StartTaskRequest, StartTaskResponse
from benchmark.shared.dogefuzz.exceptions import RequestFailedException


class DogefuzzClient():
    """this class represents a class that communicates with dogefuzz api
    """

    def __init__(self, endpoint: str, timeout: int) -> None:
        self._endpoint = endpoint
        self._timeout = timeout

    def start_task(self, req: StartTaskRequest) -> StartTaskResponse:
        """sends the request to dogefuzz to start fuzzing
        """
        payload = req.to_json()
        res = requests.post(f"${self._endpoint}/tasks",
                            data=payload, timeout=self._timeout)
        if res.status_code != 200:
            raise RequestFailedException(
                f"not valid response ${res.status_code}")
        body_content = res.json()
        return StartTaskResponse.from_json(body_content)
