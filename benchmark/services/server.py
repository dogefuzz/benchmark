"""
this module contains the service related with HTTP server operations
"""
from multiprocessing import Process
from flask import Flask
from benchmark.server.app import app
from benchmark.shared.singleton import SingletonMeta


class ServerService(metaclass=SingletonMeta):
    """
    this service contains operations with HTTP server
    """

    def __init__(self) -> None:
        self._server: Flask = app
        self._thread: Process = None

    def start(self) -> None:
        """
        starts the Flask server
        """
        self._thread = Process(target=self._start_server)
        self._thread.start()

    def stop(self) -> None:
        """
        shutdown the Flask server
        """
        self._thread.terminate()

    def _start_server(self):
        self._server.run(host="0.0.0.0", debug=False, use_reloader=False)
