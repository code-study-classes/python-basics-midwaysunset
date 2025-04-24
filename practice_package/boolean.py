def check_between_numbers(A: int, B: int, C: int) -> bool:
    return (A < B < C) or (C < B < A)


def check_odd_three(number: int) -> bool:
    return (100 <= abs(number) <= 999) and (number % 2 != 0)


def check_unique_digits(number: int) -> bool:
    if not (100 <= abs(number) <= 999):
        return False
    digits = str(abs(number))
    return len(set(digits)) == 3


def check_palindrome_number(number: int) -> bool:
    s = str(abs(number))
    return s == s[::-1]


def check_ascending_digits(number: int) -> bool:
    if not (100 <= abs(number) <= 999):
        return False
    digits = [int(d) for d in str(abs(number))]
    return digits[0] < digits[1] < digits[2]