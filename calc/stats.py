import math

MAX_COUNT = 20
MAX_ABS = 10000


def validate_values(values):
    """Проверить список чисел после чтения входных данных."""
    if not values:
        raise ValueError("ОШИБКА: последовательность пуста")

    if len(values) > MAX_COUNT:
        raise ValueError("ОШИБКА: слишком много чисел (максимум 20)")

    for value in values:
        if not math.isfinite(value):
            raise ValueError("ОШИБКА: число должно быть конечным")
        if abs(value) > MAX_ABS:
            raise ValueError("ОШИБКА: значение вне допустимого диапазона")


def count(values):
    return len(values)


def total(values):
    result = 0.0
    for value in values:
        result += value
    return result


def mean(values):
    return total(values) / len(values)


def sum_squares(values):
    result = 0.0
    for value in values:
        result += value ** 2
    return result


def rms(values):
    return math.sqrt(sum_squares(values) / len(values))


def sum_squared_deviations(values):
    average = mean(values)
    result = 0.0
    for value in values:
        result += (value - average) ** 2
    return result


def variance(values):
    return sum_squared_deviations(values) / len(values)


def stddev_population(values):
    return math.sqrt(variance(values))


def stddev_sample(values):
    if len(values) < 2:
        return None
    return math.sqrt(sum_squared_deviations(values) / (len(values) - 1))


def minimum(values):
    result = values[0]
    for value in values:
        if value < result:
            result = value
    return result


def maximum(values):
    result = values[0]
    for value in values:
        if value > result:
            result = value
    return result


def positive_count(values):
    result = 0
    for value in values:
        if value > 0:
            result += 1
    return result


def negative_count(values):
    result = 0
    for value in values:
        if value < 0:
            result += 1
    return result


REPORT = [
    ("Количество", count, 0),
    ("Сумма", total, 3),
    ("Ср. арифм.", mean, 3),
    ("Сумма кв.", sum_squares, 3),
    ("Ср. кв.", rms, 3),
    ("Дисперсия", variance, 3),
    ("СКО", stddev_population, 3),
    ("Станд. откл.", stddev_sample, 3),
    ("Наименьшее", minimum, 3),
    ("Наибольшее", maximum, 3),
    ("Положительных", positive_count, 0),
    ("Отрицательных", negative_count, 0),
]