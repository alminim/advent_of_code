from pathlib import Path
from typing import List


def parse_input(input_file: Path) -> List[List[int]]:
    parsed_reports: List[List[int]] = list()
    for line in input_file.read_text().splitlines():
        parsed_reports.append(list(map(int, line.split())))
    return parsed_reports


def main():
    input_file = Path(Path(__file__).parent, "input.txt")
    parsed_input = parse_input(input_file)
    print(parsed_input)


if __name__ == "__main__":
    main()
