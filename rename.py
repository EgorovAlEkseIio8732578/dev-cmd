import argparse
import sys
from pathlib import Path

parser = argparse.ArgumentParser(
    prog="rename",
    description="Переименование файлов, список которых приходит на стандартный вход",
)
parser.add_argument("--pattern", required=True)
args = parser.parse_args()

number = 1
for line in sys.stdin:
    name = line.strip()
    if not name:
        continue
    new_name = args.pattern.replace("{n}", f"{number:03}")
    Path(name).rename(new_name)
    print(new_name)
    number += 1
