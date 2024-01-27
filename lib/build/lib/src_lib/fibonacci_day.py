from datetime import datetime


__all__ = [
    'get_day',
    'fibonacci_recursive',
    'get_fibonacci_day'
]


def get_day() -> int:
    now = datetime.now()
    return now.day


def fibonacci_recursive(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def get_fibonacci_day(day: int = get_day()) -> int:
    return fibonacci_recursive(day + 1)
