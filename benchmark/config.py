from benchmark.shared.singleton import SingletonMeta


class Config(metaclass=SingletonMeta):

    def __init__(self) -> None:
        self.contracts_zip_url: str = "https://drive.google.com/file/d/1y43UDNO-5kRaxsvbTseuIkwYYa33K6_e/view?usp=share_link"
        self.contracts_folder: str = ".temp"
