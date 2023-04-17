"""
this module contains the exceptions used by this project
"""


class ContractsNotFoundException(Exception):
    """the exception is raised when the contracts folder doesn't exist
    """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class InvalidFuzzingType(Exception):
    """this exception is raised when an invalid fuzzing type is provided
    """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class InvalidDuration(Exception):
    """this exception is raised when an invalid duration is provided
    """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class ContractNotFoundException(Exception):
    """this exception will be raised when the contract is not found
    """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
