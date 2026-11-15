import argparse

from calc.integration import FUNCTIONS
from calc.series import FORMULAS


def build_parser():
    parser = argparse.ArgumentParser(
        prog="mathtool",
        description="Консольное приложение для математических расчётов.",
        allow_abbrev=False,
    )

    subparsers = parser.add_subparsers(dest="command")

    solve_parser = subparsers.add_parser(
        "solve",
        help="решение уравнения A*x^2 + B*x + C = 0",
        allow_abbrev=False,
    )
    solve_parser.add_argument("-a", type=int, default=None, help="коэффициент A")
    solve_parser.add_argument("-b", type=int, default=None, help="коэффициент B")
    solve_parser.add_argument("-c", type=int, default=None, help="коэффициент C")

    stats_parser = subparsers.add_parser(
        "stats",
        help="статистика числовой последовательности",
        allow_abbrev=False,
    )
    stats_parser.add_argument(
        "--input",
        help="файл с числами; без параметра читается стандартный ввод",
    )

    series_parser = subparsers.add_parser(
        "series",
        help="сумма знакочередующегося ряда",
        allow_abbrev=False,
    )
    series_parser.add_argument("--func", choices=sorted(FORMULAS), required=True)
    series_group = series_parser.add_mutually_exclusive_group(required=True)
    series_group.add_argument("--terms", type=int, help="количество слагаемых")
    series_group.add_argument("--eps", type=float, help="точность по последнему слагаемому")

    integrate_parser = subparsers.add_parser(
        "integrate",
        help="численное интегрирование",
        allow_abbrev=False,
    )
    integrate_parser.add_argument("--func", choices=sorted(FUNCTIONS), required=True)
    integrate_parser.add_argument("--from", dest="start", type=float, required=True)
    integrate_parser.add_argument("--to", dest="end", type=float, required=True)
    integrate_parser.add_argument("--steps", type=int, required=True)

    return parser