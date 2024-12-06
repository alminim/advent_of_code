from pathlib import Path
import re
from typing import Iterable


VALID_INSTRUCTION = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")


def parse_input(input_file: Path) -> Iterable[re.Match]:
    return re.finditer(VALID_INSTRUCTION, input_file.read_text())


def main():
    input_file = Path(Path(__file__).parent, "input.txt")
    matches = parse_input(input_file)
    total = 0
    for match in matches:
        total += int(match.group(1)) * int(match.group(2))

    print(total)


if __name__ == "__main__":
    main()
