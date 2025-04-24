def calculate_distance(x1: float, x2: float) -> float:
    return abs(x2 - x1)


def calculate_segments(length_a: float, length_b: float) -> int:
    return length_a // length_b


def calculate_digit_sum(number: int) -> int:
    return sum(int(digit) for digit in str(abs(number)))


def calculate_rect_area(x1: float, y1: float, x2: float, y2: float) -> float:
    return abs(x2 - x1) * abs(y2 - y1)


def round_to_multiple(number: float, multiple: float) -> float:
    return round(number / multiple) * multiple