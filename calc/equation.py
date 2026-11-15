import math

MAX_VALUE = 10000


def validate_coefficients(a, b, c):
    """Проверить коэффициенты уравнения."""
    if abs(a) > MAX_VALUE:
        raise ValueError("ОШИБКА: коэффициент A вне допустимого диапазона")
    if abs(b) > MAX_VALUE:
        raise ValueError("ОШИБКА: коэффициент B вне допустимого диапазона")
    if abs(c) > MAX_VALUE:
        raise ValueError("ОШИБКА: коэффициент C вне допустимого диапазона")


def solve(a, b, c):
    """Вернуть вид уравнения, дискриминант и список действительных корней."""
    if a == 0:
        if b == 0:
            raise ValueError("ОШИБКА: это не уравнение, неизвестное отсутствует")
        return "линейное", None, [-c / b]

    discriminant = b * b - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return "квадратное", discriminant, [root1, root2]

    if discriminant == 0:
        root = -b / (2 * a)
        return "квадратное", discriminant, [root]

    return "квадратное", discriminant, []