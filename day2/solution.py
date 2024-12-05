from pathlib import Path
from typing import List


def parse_input(input_file: Path) -> List[List[int]]:
    parsed_reports: List[List[int]] = list()
    for line in input_file.read_text().splitlines():
        parsed_reports.append(list(map(int, line.split())))
    return parsed_reports


def check_safety(report: List[int]) -> bool:
    is_ascending = report[0] < report[len(report) - 1]
    for i in range(len(report) - 1):
        if not (1 <= abs(report[i] - report[i + 1]) <= 3) or (
            is_ascending != (report[i] < report[i + 1])
        ):
            if not (1 <= abs(report[i - 1] - report[i + 1]) <= 3) or (
                is_ascending != (report[i - 1] < report[i + 1])
            ):
                return False
    return True


def count_num_safe_reports(reports: List[List[int]]) -> int:
    total_safe_reports = 0
    for report in reports:
        if check_safety(report):
            total_safe_reports += 1
    return total_safe_reports


def main():
    input_file = Path(Path(__file__).parent, "input.txt")
    parsed_input = parse_input(input_file)
    print(count_num_safe_reports(parsed_input))


if __name__ == "__main__":
    main()
