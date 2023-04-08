"""
this modules contains information about the requests to the dogefuzz client
"""
import json


class StartTaskRequest():
    """represents the request to start the fuzzing request in dogefuzz
    """

    def __init__(
        self,
        contract_source: str,
        contract_name: str,
        arguments: list,
        duration: str,
        detectors: list,
        fuzzing_type: str
    ) -> None:
        self._contract_source = contract_source
        self._contract_name = contract_name
        self._arguments = arguments
        self._duration = duration
        self._detectors = detectors
        self._fuzzing_type = fuzzing_type

    def to_json(self) -> str:
        """serializes object to json
        """
        content = {
            "contractSource": self._contract_source,
            "contractName": self._contract_name,
            "arguments": self._arguments,
            "duration": self._duration,
            "detectors": self._detectors,
            "fuzzingType": self._fuzzing_type,
        }
        return json.dumps(content)


class StartTaskResponse():
    """represents the response after starting a fuzzing task in dogefuzz
    """

    def __init__(self, task_id: str) -> None:
        self._task_id = task_id

    @property
    def task_id(self):
        """task_id property
        """
        return self._task_id

    @classmethod
    def from_json(cls, json_content: map):
        """deserializes object from json
        """
        return StartTaskResponse(task_id=json_content["taskId"])


class TimeSeriesData():
    """represents a chart information
    """

    def __init__(self, x_axis: list, y_axis: list) -> None:
        self._x_axis = x_axis
        self._y_axis = y_axis

    @property
    def x_axis(self):
        """x_axis property
        """
        return self._x_axis

    @property
    def y_axis(self):
        """y_axis property
        """
        return self._y_axis

    def to_dict(self):
        """gets dictionary representation
        """
        return {
            "x": self._x_axis,
            "y": self._y_axis,
        }

    @classmethod
    def from_json(cls, json_content: map):
        """deserializes object from json
        """
        return TimeSeriesData(x_axis=json_content["x"], y_axis=json_content["y"])


class TransactionReport():
    """represents the detailed information of each transaction in the fuzzing task
    """

    def __init__(
        self,
        timestamp: str,
        blockchain_hash: str,
        inputs: list,
        detected_weaknesses: list,
        executed_instructions: list,
        delta_coverage: int,
        delta_min_distance: int,
    ) -> None:
        self._timestamp = timestamp
        self._blockchain_hash = blockchain_hash
        self._inputs = inputs
        self._detected_weaknesses = detected_weaknesses
        self._executed_instructions = executed_instructions
        self._delta_coverage = delta_coverage
        self._delta_min_distance = delta_min_distance

    @property
    def timestamp(self):
        """timestamp property
        """
        return self._timestamp

    @property
    def blockchain_hash(self):
        """blockchain_hash property
        """
        return self._blockchain_hash

    @property
    def inputs(self):
        """inputs property
        """
        return self._inputs

    @property
    def detected_weaknesses(self):
        """detected_weaknesses property
        """
        return self._detected_weaknesses

    @property
    def executed_instructions(self):
        """executed_instructions property
        """
        return self._executed_instructions

    @property
    def delta_coverage(self):
        """delta_coverage property
        """
        return self._delta_coverage

    @property
    def delta_min_distance(self):
        """delta_min_distance property
        """
        return self._delta_min_distance

    def to_dict(self):
        """gets dictionary representation
        """
        return {
            "timestamp": self._timestamp,
            "blockchainHash": self._blockchain_hash,
            "inputs": self._inputs,
            "detectedWeaknesses": self._detected_weaknesses,
            "executedInstructions": self._executed_instructions,
            "delta_coverage": self._delta_coverage,
            "delta_min_distance": self._delta_min_distance
        }

    @classmethod
    def from_json(cls, json_content: map):
        """deserializes object from json
        """
        return TransactionReport(
            timestamp=json_content["timestamp"],
            blockchain_hash=json_content["blockchainHash"],
            inputs=json_content["inputs"],
            detected_weaknesses=json_content["detectedWeaknesses"],
            executed_instructions=json_content["executedInstructions"],
            delta_coverage=json_content["deltaCoverage"],
            delta_min_distance=json_content["deltaMinDistance"],
        )


class TaskReport():
    """represents the response of the webhook when the fuzzing task finishes
    """

    def __init__(
        self,
        task_id: str,
        time_elapsed: str,
        contract_name: str,
        total_instructions: int,
        coverage: int,
        coverage_by_time: TimeSeriesData,
        min_distance: int,
        min_distance_by_time: TimeSeriesData,
        transactions: list,
        detected_weaknesses: list
    ) -> None:
        self._task_id = task_id
        self._time_elapsed = time_elapsed
        self._contract_name = contract_name
        self._total_instructions = total_instructions
        self._coverage = coverage
        self._coverage_by_time = coverage_by_time
        self._min_distance = min_distance
        self._min_distance_by_time = min_distance_by_time
        self._transactions = transactions
        self._detected_weaknesses = detected_weaknesses

    @property
    def task_id(self):
        """task_id property
        """
        return self._task_id

    @property
    def time_elapsed(self):
        """time_elapsed property
        """
        return self._time_elapsed

    @property
    def contract_name(self):
        """contract_name property
        """
        return self._contract_name

    @property
    def total_instructions(self):
        """total_instructions property
        """
        return self._total_instructions

    @property
    def coverage(self):
        """coverage property
        """
        return self._coverage

    @property
    def coverage_by_time(self):
        """coverage_by_time property
        """
        return self._coverage_by_time

    @property
    def min_distance(self):
        """min_distance property
        """
        return self._min_distance

    @property
    def min_distance_by_time(self):
        """min_distance_by_time property
        """
        return self._min_distance_by_time

    @property
    def transactions(self):
        """transactions property
        """
        return self._transactions

    @property
    def detected_weaknesses(self):
        """detected_weaknesses property
        """
        return self._detected_weaknesses

    def to_dict(self):
        """gets dictionary representation
        """
        return {
            "taskId": self._task_id,
            "timeElapsed": self._time_elapsed,
            "contractName": self._contract_name,
            "totalInstructions": self._total_instructions,
            "coverage": self._coverage,
            "minDistance": self._min_distance,
            "detectedWeaknesses": self._detected_weaknesses,
            "coverageByTime": self._coverage_by_time.to_dict(),
            "minDistanceByTime": self._min_distance_by_time.to_dict(),
            "transactions": [t.to_dict() for t in self._transactions],
        }

    @classmethod
    def from_json(cls, json_content: map):
        """deserializes object form json
        """
        transactions = []
        for transaction_json in json_content["transactions"]:
            transaction = TransactionReport.from_json(transaction_json)
            transactions.append(transaction)
        return TaskReport(
            task_id=json_content["taskId"],
            time_elapsed=json_content["timeElapsed"],
            contract_name=json_content["contractName"],
            total_instructions=json_content["totalInstructions"],
            coverage=json_content["coverage"],
            coverage_by_time=TimeSeriesData.from_json(
                json_content["coverageByTime"]),
            min_distance=json_content["minDistance"],
            min_distance_by_time=TimeSeriesData.from_json(
                json_content["minDistanceByTime"]),
            transactions=transactions,
            detected_weaknesses=json_content["detectedWeaknesses"],
        )
