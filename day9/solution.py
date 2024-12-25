from pathlib import Path
from copy import deepcopy
from typing import List, Union


EMPTY_BLOCK = "."


def parse_input(input_file: Path) -> List[List[Union[str, int]]]:
    """
    List of lists in the format of [file id, size]
    """
    disk_map = input_file.read_text()
    disk: List[List[Union[str, int]]] = []

    for i, block_size in enumerate(disk_map):
        if i % 2 == 0:
            disk.append([str(i // 2), int(block_size)])
        else:
            disk.append([".", int(block_size)])

    return disk


def move_file(
    disk: List[List[Union[str, int]]],
    file_to_move: List[Union[str, int]],
    new_location: int,
) -> List[List[Union[str, int]]]:
    space_to_replace = disk[new_location]
    if file_to_move[1] < space_to_replace[1]:
        disk.insert(
            new_location + 1, [EMPTY_BLOCK, space_to_replace[1] - file_to_move[1]]
        )

    disk[new_location] = file_to_move
    return disk


def find_absolute_position(
    disk: List[List[Union[str, int]]], current_file_location: int
) -> int:
    position = 0
    for i in range(current_file_location):
        position += disk[i][1]

    return position


def fill_empty_space(disk: List[List[Union[str, int]]]) -> List[List[Union[str, int]]]:
    new_disk: List[List[Union[str, int]]] = deepcopy(disk)
    absolute_position = find_absolute_position(disk, len(disk))
    for file in disk[::-1]:
        absolute_position -= file[1]
        if file[0] == EMPTY_BLOCK:
            continue
        new_absolute_position = 0
        for new_location, copied_file in enumerate(new_disk):
            if new_absolute_position >= absolute_position:
                break
            if copied_file[0] == EMPTY_BLOCK and file[1] <= copied_file[1]:
                new_disk = move_file(new_disk, file, new_location)
                new_disk[new_disk.index(file, new_location + 1)][0] = EMPTY_BLOCK
                break
            new_absolute_position += copied_file[1]
    return new_disk


def calculate_checksum(disk: List[List[Union[str, int]]]) -> int:
    checksum = 0
    absolute_position = 0
    for file in disk:
        for i in range(file[1]):
            checksum += (
                absolute_position * int(file[0]) if file[0] != EMPTY_BLOCK else 0
            )
            absolute_position += 1
    return checksum


def main():
    input_file = Path(Path(__file__).parent, "input.txt")
    parsed_input = parse_input(input_file)
    filled_disk = fill_empty_space(parsed_input)
    print(calculate_checksum(filled_disk))


if __name__ == "__main__":
    main()
