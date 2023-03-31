"""this module contains class that will describe the testing process
"""


from benchmark.shared.utils import validate_duration, validate_fuzzing_types


class Entry():
    """represents a single testing entry, which is a single execution of the dogefuzz
    """

    def __init__(self, contract: str, args: list, duration: str, fuzzing_types: list, times: int) -> None:
        self.contract = contract
        self.args = args
        self.duration = duration
        self.fuzzing_types = fuzzing_types
        self.times = times


class Request():
    """represents the testing request containing the set of tests to be made
    """

    def __init__(self, entries: list) -> None:
        self.entries: list = entries


class RequestFactory():
    """
    represents the factory pattern to create the Request instance
    """

    @classmethod
    def from_contracts_list(cls, contracts: list, duration: str, fuzzing_types: list, times: int) -> Request:
        """creates the Request class from a list of contracts
        """
        validate_duration(duration)
        validate_fuzzing_types(fuzzing_types)

        testing_entries = []
        for contract in contracts:
            entry = Entry(contract["name"], [], duration, fuzzing_types, times)
            testing_entries.append(entry)
        return Request(testing_entries)

    @classmethod
    def from_script(cls, script_content: map) -> Request:
        """creates the Request class from the script.json content
        """
        duration = script_content["duration"]
        fuzzing_types = script_content["fuzzingTypes"]
        times = script_content["times"]

        validate_duration(duration)
        validate_fuzzing_types(fuzzing_types)

        testing_entries = []
        for entry in script_content["contracts"]:
            entry = Entry(
                entry["name"],
                entry["arguments"],
                duration,
                fuzzing_types,
                times
            )
            testing_entries.append(entry)
        return Request(testing_entries)
