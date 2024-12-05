from pathlib import Path
from typing import Tuple, List


def parse_input(input_file: Path) -> Tuple[List[int], List[int]]:
    first_list: List[int] = list()
    second_list: List[int] = list()
    for line in input_file.read_text().splitlines():
        first_number, second_number = line.split()
        first_list.append(int(first_number))
        second_list.append(int(second_number))
    
    return first_list, second_list


def main():
    input_file = Path(Path(__file__).parent, 'input.txt')
    first_list, second_list = parse_input(input_file)
    total_distance = 0
    for _ in range(min(len(first_list), len(second_list))):
        first_min = min(first_list)
        second_min = min(second_list)

        first_list.remove(first_min)
        second_list.remove(second_min)

        total_distance += abs(first_min - second_min)
    
    print(total_distance)

    


if __name__ == '__main__':
    main()

