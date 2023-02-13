"""
Main module
"""
import fire

from benchmark.benchmark import Benchmark


def main():
    """
    Project entrypoint
    """
    fire.Fire(Benchmark)
