from datetime import timedelta


SECONDS_MULTIPLER = {
    'd': 60 * 60 * 24,
    'h': 60 * 60,
    'm': 60,
    's': 1,
}


def parse_timedelta(duration: str) -> timedelta:
    case_insensitive_duration = duration.lower()
    total_seconds = 0
    prev_num = []
    for character in case_insensitive_duration:
        if character.isalpha():
            total_seconds = _convert_number_in_seconds(
                character, ''.join(prev_num), total_seconds)
            prev_num = []
        elif character.isnumeric() or character == '.':
            prev_num.append(character)
    return timedelta(seconds=total_seconds)


def _convert_number_in_seconds(character: str, number_str: str, total_amount: int) -> int:
    if number_str == "":
        return 0
    number = int(number_str)
    return total_amount + number * SECONDS_MULTIPLER[character]
