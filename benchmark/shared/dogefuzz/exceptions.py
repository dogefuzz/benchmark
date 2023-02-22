"""
this module contains the exception that could be raised in the communication
between this project and dogefuzz api
"""


class RequestFailedException(Exception):
    """this exception will be raised when the request to dogefuzz api is not
    succesful
    """

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
