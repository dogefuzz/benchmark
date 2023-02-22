"""
this module contains useful methods used in other parts of the project
"""
from benchmark.shared.constants import DURATION_10M, DURATION_15M, DURATION_30M, DURATION_5M, FUZZING_TYPE_BLACKBOX_FUZZING, FUZZING_TYPE_DIRECTED_GREYBOX_FUZZING, FUZZING_TYPE_GREYBOX_FUZZING
from benchmark.shared.exceptions import InvalidDuration, InvalidFuzzingType


def validate_fuzzing_type(fuzzing_type: str) -> None:
    """validates the fuzzing type string
    """
    valid_values = [
        FUZZING_TYPE_BLACKBOX_FUZZING,
        FUZZING_TYPE_GREYBOX_FUZZING,
        FUZZING_TYPE_DIRECTED_GREYBOX_FUZZING,
    ]
    if fuzzing_type not in valid_values:
        raise InvalidFuzzingType("an invalid fuzzing type was provided")


def validate_duration(duration: str) -> None:
    """validates the duration string
    """
    valid_values = [
        DURATION_5M,
        DURATION_10M,
        DURATION_15M,
        DURATION_30M,
    ]
    if duration not in valid_values:
        raise InvalidDuration("an invalid duration was provided")
