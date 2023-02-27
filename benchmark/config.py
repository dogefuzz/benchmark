"""
this module contains the class related to the project configuration
"""
from benchmark.shared.singleton import SingletonMeta


class Config(metaclass=SingletonMeta):
    """this class represent the configuration of the project
    """

    def __init__(self) -> None:
        self.contracts_zip_url: str = "https://drive.google.com/file/d/1y43UDNO-5kRaxsvbTseuIkwYYa33K6_e/view?usp=share_link"
        self.contracts_folder: str = ".temp"
        self.script_path: str = "script.json"
        self.dogefuzz_endpoint: str = "http://dogefuzz:3456"
        self.dogefuzz_timeout: int = 30
        self.detectors: list = ["delegate", "exception-disorder", "gasless-send",
                                "number-dependency", "reentrancy", "timestamp-dependency"]
