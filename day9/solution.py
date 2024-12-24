from pathlib import Path
from typing import List, Dict, Set, Tuple


EMPTY_BLOCK = "."


def parse_input(input_file: Path) -> List[str]:
    disk_map = input_file.read_text()
    disk: List[str] = []

    for i, block_size in enumerate(disk_map):
        if i % 2 == 0:
            disk.extend([str(int(i / 2))] * int(block_size))
        else:
            disk.extend([EMPTY_BLOCK] * int(block_size))

    return disk


def fill_empty_space(disk: List[str]) -> List[str]:
    last_nonempty_block = -1
    for i in range(len(disk)):
        if disk[i] != EMPTY_BLOCK:
            continue

        while disk[last_nonempty_block] == EMPTY_BLOCK:
            last_nonempty_block -= 1

        if len(disk) + last_nonempty_block <= i:
            return disk

        disk[i], disk[last_nonempty_block] = disk[last_nonempty_block], disk[i]


def calculate_checksum(disk: List[str]) -> int:
    checksum = 0
    for i, block in enumerate(disk):
        checksum += int(block) * i if block != EMPTY_BLOCK else 0
    return checksum


def main():
    input_file = Path(Path(__file__).parent, "input.txt")
    parsed_input = parse_input(input_file)
    filled_disk = fill_empty_space(parsed_input)
    print(calculate_checksum(filled_disk))


if __name__ == "__main__":
    main()
