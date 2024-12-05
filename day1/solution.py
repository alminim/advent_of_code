from pathlib import Path
from typing import Tuple, List


def parse_input(input_file: Path) -> Tuple[List[int], List[int]]:
    first_list: List[int] = list()
    second_list: List[int] = list()
    for line in input_file.read_text().splitlines():
        first_number, second_number = line.split()
        first_list.append(first_number)
        second_list.append(second_number)
    
    return first_list, second_list


def main():
    input_file = Path(Path(__file__).parent, 'input.txt')
    parsed_input = parse_input(input_file)
    print(parsed_input)


if __name__ == '__main__':
    main()

