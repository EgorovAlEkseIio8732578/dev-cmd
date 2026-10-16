"""
mathtool — консольное приложение для решения алгебраических уравнений
вида A*x^2 + B*x + C = 0.

Запуск:
    python mathtool.py                         вывод справки
    python mathtool.py --help                  вывод справки
    python mathtool.py solve                   ввод коэффициентов с клавиатуры
    python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами

Коэффициенты A, B, C — целые числа, по модулю не превышающие MAX_VALUE.
"""

import sys
import math

MAX_VALUE = 20000


def print_help():
    print("mathtool — решение уравнений вида A*x^2 + B*x + C = 0")
    print()
    print("Использование:")
    print("    python mathtool.py                         вывод справки")
    print("    python mathtool.py --help                  вывод справки")
    print("    python mathtool.py solve                   ввод коэффициентов с клавиатуры")
    print("    python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами")
    print()
    print(f"Коэффициенты A, B, C — целые числа, по модулю не превышающие {MAX_VALUE}.")


def parse_arguments(args):
    if len(args) == 0 or args[0] == "--help":
        print_help()
        sys.exit(0)

    if args[0] != "solve":
        print("ОШИБКА: неизвестная команда", file=sys.stderr)
        sys.exit(1)

    if len(args) == 1:
        a_str = input("Введите A: ")
        b_str = input("Введите B: ")
        c_str = input("Введите C: ")

    elif len(args) == 7:
        print(args)
        if args[1] != "-a" or args[3] != "-b" or args[5] != "-c":
            print("ОШИБКА: неизвестный параметр", file=sys.stderr)
            sys.exit(1)
        a_str, b_str, c_str = args[2], args[4], args[6]

    else:
        print("ОШИБКА: неверный набор параметров", file=sys.stderr)
        sys.exit(1)

    return a_str, b_str, c_str


def convert_to_int(a_str, b_str, c_str):
    try:
        a = int(a_str)
        b = int(b_str)
        c = int(c_str)
    except ValueError:
        print("ОШИБКА: коэффициент не является целым числом", file=sys.stderr)
        sys.exit(1)
    return a, b, c

def validate_range(a, b, c):
    
    if abs(a) > MAX_VALUE or abs(b) > MAX_VALUE or abs(c) > MAX_VALUE:
        print("ОШИБКА: значение вне допустимого диапазона", file=sys.stderr)
        sys.exit(1)


def solve_linear(b, c):
   
    if b != 0:
        print("Уравнение линейное")
        x = -c / b
        print(f"x = {x:.3f}")
    else:
        
        print("ОШИБКА: это не уравнение, неизвестное отсутствует", file=sys.stderr)
        sys.exit(1)


def solve_quadratic(a, b, c):
    
    print("Уравнение квадратное")

    d = b * b - 4 * a * c
    print(f"D = {d}")

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f"x1 = {x1:.3f}")
        print(f"x2 = {x2:.3f}")
    elif d == 0:
        x = -b / (2 * a)
        print(f"x = {x:.3f}")
    else:
        print("Действительных корней нет")


def solve(a, b, c):
  
    if a == 0:
        solve_linear(b, c)
    else:
        solve_quadratic(a, b, c)



def main():
    a_str, b_str, c_str = parse_arguments(sys.argv[1:])
    a, b, c = convert_to_int(a_str, b_str, c_str)
    validate_range(a, b, c)
    solve(a, b, c)
    sys.exit(0)

if __name__ == "__main__":
    main()
