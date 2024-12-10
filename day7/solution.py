from itertools import product
from pathlib import Path
from typing import List, Dict, Set
from simpleeval import simple_eval


VALID_OPERATORS = {"+", "*"}


def parse_input(input_file: Path) -> Dict[int, List[str]]:
    equations = input_file.read_text().splitlines()
    return {
        int(equation.split(":")[0]): equation.split(":")[1].split()
        for equation in equations
    }


def calculate_equation(values: List[str], operators: str) -> int:
    total = simple_eval(operators[0].join(values[:2]))
    values = values[2:]
    operators = operators[1:]

    for value in values:
        total = simple_eval(str(total) + operators[0] + str(value))
        operators = operators[1:]

    return total


def calculate_all_evaluations(values: List[str]) -> Set[int]:
    total_operators = len(values) - 1
    possible_evaluations: Set[int] = set()
    for operator_combination in product(VALID_OPERATORS, repeat=total_operators):
        possible_evaluations.add(calculate_equation(values, operator_combination))

    return possible_evaluations


def main():
    input_file = Path(Path(__file__).parent, "input.txt")
    parsed_input = parse_input(input_file)

    total_of_valid_evaluations = 0
    for desired_evaluation, values in parsed_input.items():
        if desired_evaluation in calculate_all_evaluations(values):
            total_of_valid_evaluations += desired_evaluation

    print(total_of_valid_evaluations)


if __name__ == "__main__":
    main()
