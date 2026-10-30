import sys

from calc import equation, integration, series, stats
from cli import build_parser


def read_values(input_path):
    #Прочитать числа из файла или стандартного ввода
    values = []

    if input_path:
        try:
            with open(input_path, encoding="utf-8-sig") as handle:
                sources = handle
                _read_lines(values, sources)
        except OSError as error:
            raise ValueError("ОШИБКА: файл не открывается") from error
    else:
        _read_lines(values, sys.stdin)

    stats.validate_values(values)
    return values


def _read_lines(values, source):
    for line in source:
        for word in line.split():
            try:
                values.append(float(word))
            except ValueError as error:
                raise ValueError(f"ОШИБКА: {word} не является числом") from error


def process_solve(args):
    supplied = [args.a is not None, args.b is not None, args.c is not None]
    if any(supplied) and not all(supplied):
        raise ValueError("ОШИБКА: укажите все три коэффициента либо ни одного")

    if not any(supplied):
        a = int(input("Введите A: "))
        b = int(input("Введите B: "))
        c = int(input("Введите C: "))
    else:
        a, b, c = args.a, args.b, args.c

    equation.validate_coefficients(a, b, c)
    kind, discriminant, roots = equation.solve(a, b, c)

    if kind == "линейное":
        print("Уравнение линейное")
        print(f"x = {roots[0]:.3f}")
        return 0

    print("Уравнение квадратное")
    print(f"D = {discriminant}")

    if len(roots) == 2:
        print(f"x1 = {roots[0]:.3f}")
        print(f"x2 = {roots[1]:.3f}")
    elif len(roots) == 1:
        print(f"x = {roots[0]:.3f}")
    else:
        print("Действительных корней нет")

    return 0


def process_stats(args):
    values = read_values(args.input)

    for label, function, decimals in stats.REPORT:
        value = function(values)
        if value is None:
            print(f"{label}: НЕ СУЩЕСТВУЕТ")
        elif decimals == 0:
            print(f"{label}: {value}")
        else:
            print(f"{label}: {value:.{decimals}f}")

    return 0


def process_series(args):
    term_function, formula = series.FORMULAS[args.func]

    if args.terms is not None:
        term_count, result = series.sum_by_terms(term_function, args.terms)
    else:
        term_count, result = series.sum_by_eps(term_function, args.eps)

    print(formula)
    print(f"Слагаемых: {term_count}")
    print(f"Сумма ряда: {result:.4f}")
    return 0


def process_integrate(args):
    info = integration.FUNCTIONS[args.func]
    integration.validate_steps(args.steps)
    integration.validate_limits(args.start, args.end, info)

    result = integration.integrate(
        info["function"],
        args.start,
        args.end,
        args.steps,
    )

    print(info["formula"])
    print(f"Значение интеграла: {result:.4f}")
    return 0


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return 0

    try:
        if args.command == "solve":
            return process_solve(args)
        if args.command == "stats":
            return process_stats(args)
        if args.command == "series":
            return process_series(args)
        if args.command == "integrate":
            return process_integrate(args)
    except (ValueError, EOFError) as error:
        print(str(error), file=sys.stderr)
        return 1

    print("ОШИБКА: неизвестная команда", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
