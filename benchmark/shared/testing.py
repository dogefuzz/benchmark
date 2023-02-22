"""this module contains class that will describe the testing process
"""


class Entry():
    """represents a single testing entry, which is a single execution of the dogefuzz
    """

    def __init__(self, contract: str, args: list, duration: str, fuzzing_type: str) -> None:
        self.contract = contract
        self.args = args
        self.duration = duration
        self.fuzzing_type = fuzzing_type


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
    def from_contracts_list(cls, contracts: list, duration: str, fuzzing_type: str) -> Request:
        """creates the Request class from a list of contracts
        """
        testing_entries = []
        for contract in contracts:
            entry = Entry(contract["name"], [], duration, fuzzing_type)
            testing_entries.append(entry)
        return Request(testing_entries)

    @classmethod
    def from_script(cls, script_content: map) -> Request:
        """creates the Request class from the script.json content
        """
        testing_entries = []
        for entry in script_content:
            entry = Entry(
                entry["name"],
                entry["arguments"],
                entry["duration"],
                entry["fuzzing_type"]
            )
            testing_entries.append(entry)
        return Request(testing_entries)
