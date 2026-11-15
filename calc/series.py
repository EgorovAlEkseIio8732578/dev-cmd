import math

MAX_TERMS = 10000
MAX_EPS = 0.0001
MAX_ITERATIONS = 100000


def sign(n):
    return 1 if n % 2 == 1 else -1


def term_sqplus(n):
    return sign(n) / (n * n + 1)


def term_third(n):
    return sign(n) / (3 * n)


FORMULAS = {
    "sqplus": (
        term_sqplus,
        "S = 1/(1^2+1) - 1/(2^2+1) + 1/(3^2+1) - ...",
    ),
    "third": (
        term_third,
        "S = 1/3 - 1/6 + 1/9 - 1/12 + ...",
    ),
}


def validate_terms(terms):
    if terms < 1 or terms > MAX_TERMS:
        raise ValueError("ОШИБКА: количество слагаемых вне диапазона")


def validate_eps(eps):
    if not math.isfinite(eps) or eps <= 0 or eps > MAX_EPS:
        raise ValueError("ОШИБКА: точность вне диапазона")


def sum_by_terms(term_function, terms):
    validate_terms(terms)
    result = 0.0
    for n in range(1, terms + 1):
        result += term_function(n)
    return terms, result


def sum_by_eps(term_function, eps):
    validate_eps(eps)
    result = 0.0

    for n in range(1, MAX_ITERATIONS + 1):
        term = term_function(n)
        result += term
        if abs(term) < eps:
            return n, result

    raise ValueError("ОШИБКА: точность не достигнута")