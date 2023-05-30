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


class TaskReport():
    """represents the response of the webhook when the fuzzing task finishes
    """

    def __init__(
        self,
        task_id: str,
        time_elapsed: str,
        contract_name: str,
        total_instructions: int,
        average_coverage: float,
        max_coverage: int,
        coverage_by_time: TimeSeriesData,
        min_distance: int,
        min_distance_by_time: TimeSeriesData,
        detected_weaknesses: list,
        critical_instructions_hits: int,
        instructions: map,
        instruction_hits_heat_map: map
    ) -> None:
        self._task_id = task_id
        self._time_elapsed = time_elapsed
        self._contract_name = contract_name
        self._total_instructions = total_instructions
        self._average_coverage = average_coverage
        self._max_coverage = max_coverage
        self._coverage_by_time = coverage_by_time
        self._min_distance = min_distance
        self._min_distance_by_time = min_distance_by_time
        self._detected_weaknesses = detected_weaknesses
        self._critical_instructions_hits = critical_instructions_hits
        self._instructions = instructions
        self._instruction_hits_heat_map = instruction_hits_heat_map

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
    def average_coverage(self):
        """average_coverage property
        """
        return self._average_coverage

    @property
    def max_coverage(self):
        """max_coverage property
        """
        return self._max_coverage

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
    def detected_weaknesses(self):
        """detected_weaknesses property
        """
        return self._detected_weaknesses

    @property
    def critical_instructions_hits(self):
        """critical_instructions_hits property
        """
        return self._critical_instructions_hits

    @property
    def instructions(self):
        """instructions property
        """
        return self._instructions

    @property
    def instruction_hits_heat_map(self):
        """instruction_hits_heat_map property
        """
        return self._instruction_hits_heat_map

    def to_dict(self):
        """gets dictionary representation
        """
        return {
            "taskId": self._task_id,
            "timeElapsed": self._time_elapsed,
            "contractName": self._contract_name,
            "totalInstructions": self._total_instructions,
            "averageCoverage": self._average_coverage,
            "maxCoverage": self._max_coverage,
            "minDistance": self._min_distance,
            "detectedWeaknesses": self._detected_weaknesses,
            "criticalInstructionsHits": self._critical_instructions_hits,
            "coverageByTime": self._coverage_by_time.to_dict(),
            "minDistanceByTime": self._min_distance_by_time.to_dict(),
            "instructions": self._instructions,
            "instructionHitsHeatMap": self._instruction_hits_heat_map,
        }

    @classmethod
    def from_json(cls, json_content: map):
        """deserializes object form json
        """
        return TaskReport(
            task_id=json_content["taskId"],
            time_elapsed=json_content["timeElapsed"],
            contract_name=json_content["contractName"],
            total_instructions=json_content["totalInstructions"],
            average_coverage=json_content["averageCoverage"],
            max_coverage=json_content["coverage"],
            coverage_by_time=TimeSeriesData.from_json(
                json_content["coverageByTime"]),
            min_distance=json_content["minDistance"],
            min_distance_by_time=TimeSeriesData.from_json(
                json_content["minDistanceByTime"]),
            detected_weaknesses=json_content["detectedWeaknesses"],
            critical_instructions_hits=json_content["criticalInstructionsHits"],
            instructions=json_content["instructions"],
            instruction_hits_heat_map=json_content["instructionHitsHeatMap"],
        )
