from pathlib import Path
import re
from typing import Iterable


VALID_INSTRUCTION = re.compile(r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))")
DO_INSTRUCTION = "do()"
DONT_INSTRUCTION = "don't()"


def parse_input(input_file: Path) -> Iterable[re.Match]:
    return re.finditer(VALID_INSTRUCTION, input_file.read_text())


def main():
    input_file = Path(Path(__file__).parent, "input.txt")
    matches = parse_input(input_file)
    total = 0
    should_count = True
    for match in matches:
        if match.group(0) == DO_INSTRUCTION:
            should_count = True
        elif match.group(0) == DONT_INSTRUCTION:
            should_count = False
        else:
            total += int(match.group(2)) * int(match.group(3)) if should_count else 0

    print(total)


if __name__ == "__main__":
    main()
