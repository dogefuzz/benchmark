"""
Main module
"""
import fire

from benchmark.cli import Benchmark


def main():
    """
    Project entrypoint
    """
    fire.Fire(Benchmark)
