import math

MAX_STEPS = 100000


def f_ratio(x):
    return x / (x + 1)


def f_root(x):
    return math.sqrt(x * x + 1)


FUNCTIONS = {
    "ratio": {
        "function": f_ratio,
        "formula": "F(x) = x / (x + 1)",
        "low": 0.0,
        "high": 20.0,
        "closed": True,
    },
    "root": {
        "function": f_root,
        "formula": "F(x) = sqrt(x^2 + 1)",
        "low": -5.0,
        "high": 5.0,
        "closed": False,
    },
}


def validate_steps(steps):
    if steps < 1 or steps > MAX_STEPS:
        raise ValueError("ОШИБКА: количество шагов вне диапазона")


def validate_limits(start, end, info):
    if not math.isfinite(start) or not math.isfinite(end):
        raise ValueError("ОШИБКА: пределы должны быть конечными числами")

    if start >= end:
        raise ValueError("ОШИБКА: начальный предел не меньше конечного")

    low = info["low"]
    high = info["high"]

    if info["closed"]:
        outside = start < low or start > high or end < low or end > high
    else:
        outside = start <= low or start >= high or end <= low or end >= high

    if outside:
        raise ValueError("ОШИБКА: предел вне промежутка")


def integrate(function, start, end, steps):
    """Вычислить интеграл методом левых прямоугольников."""
    dx = (end - start) / steps
    result = 0.0

    for i in range(steps):
        x = start + i * dx
        result += function(x) * dx

    return result