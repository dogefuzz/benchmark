"""
this module contains logic to manage script file
"""
import json

from benchmark.config import Config
from benchmark.shared.singleton import SingletonMeta
from benchmark.shared.testing import Request, RequestFactory


class ScriptService(metaclass=SingletonMeta):
    """this class represent the service responsible to operations with the script configuration
    """

    def __init__(self) -> None:
        self._config = Config()

    def read_testing_request_from_script(self) -> Request:
        """reads the script file and convert it into a Request class
        """
        with open(self._config.script_path, encoding="utf-8") as file:
            script_content = json.load(file)
            request = RequestFactory.from_script(script_content)
        return request
