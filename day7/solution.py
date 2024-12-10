from itertools import product
from pathlib import Path
from typing import List, Dict, Set, Tuple
from simpleeval import simple_eval


VALID_OPERATORS = {"+", "*", "||"}


def parse_input(input_file: Path) -> Tuple[int, List[str]]:
    equations = input_file.read_text().splitlines()
    return [
        (int(equation.split(":")[0]), equation.split(":")[1].split())
        for equation in equations
    ]


def single_calculation(values: List[str], operator: str) -> int:
    if operator != "||":
        return simple_eval(operator.join(values))
    else:
        return int("".join(values))


def calculate_equation(values: List[str], operators: Tuple[str, ...]) -> int:
    total = single_calculation(values[:2], operators[0])
    values = values[2:]
    operators = operators[1:]

    for value in values:
        total = single_calculation([str(total), value], operators[0])
        operators = operators[1:]

    return total


def can_evaluation_be_reached(desired_evaluation: int, values: List[str]) -> bool:
    total_operators = len(values) - 1
    for operator_combination in product(VALID_OPERATORS, repeat=total_operators):
        if desired_evaluation == calculate_equation(values, operator_combination):
            return True
    return False


def main():
    input_file = Path(Path(__file__).parent, "input.txt")
    parsed_input = parse_input(input_file)

    total_of_valid_evaluations = 0
    for desired_evaluation, values in parsed_input:
        if can_evaluation_be_reached(desired_evaluation, values):
            total_of_valid_evaluations += desired_evaluation

    print(total_of_valid_evaluations)


if __name__ == "__main__":
    main()
