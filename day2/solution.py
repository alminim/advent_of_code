from pathlib import Path
from typing import List


def parse_input(input_file: Path) -> List[List[int]]:
    parsed_reports: List[List[int]] = list()
    for line in input_file.read_text().splitlines():
        parsed_reports.append(list(map(int, line.split())))
    return parsed_reports


def check_safety(report: List[int]) -> bool:
    is_ascending = report[0] > report[1]
    for i in range(len(report) - 1):
        if not (1 <= abs(report[i] - report[i + 1]) <= 3) or (
            is_ascending != (report[i] > report[i + 1])
        ):
            return False
    return True


def main():
    input_file = Path(Path(__file__).parent, "input.txt")
    parsed_input = parse_input(input_file)
    for report in parsed_input:
        print(check_safety(report))


if __name__ == "__main__":
    main()
