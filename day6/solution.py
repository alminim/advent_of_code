from pathlib import Path
from typing import List, Set, Tuple

GUARD_ROTATE_ORDER = ["^", ">", "v", "<"]

GUARD_MOVE_DIRECTION = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def parse_input(input_file: Path) -> List[List[str]]:
    return [list(line) for line in input_file.read_text().splitlines()]


def find_guard(board_map: List[List[str]]) -> Tuple[int, int]:
    for i, row in enumerate(board_map):
        if any(marker in row for marker in GUARD_ROTATE_ORDER):
            for marker in GUARD_ROTATE_ORDER:
                try:
                    return i, row.index(marker)
                except ValueError:
                    continue

    return (-1, -1)


def rotate_guard(guard_marker: str) -> str:
    return GUARD_ROTATE_ORDER[
        (GUARD_ROTATE_ORDER.index(guard_marker) + 1) % len(GUARD_ROTATE_ORDER)
    ]


def move_guard(
    board_map: List[List[str]], current_pos: Tuple[int, int]
) -> List[List[str]]:
    current_marker = board_map[current_pos[0]][current_pos[1]]
    next_pos = (
        current_pos[0] + GUARD_MOVE_DIRECTION[current_marker][0],
        current_pos[1] + GUARD_MOVE_DIRECTION[current_marker][1],
    )

    if next_pos[0] >= len(board_map) or next_pos[1] >= len(board_map[0]):
        return None

    next_spot = board_map[next_pos[0]][next_pos[1]]

    if next_spot == ".":
        board_map[current_pos[0]][current_pos[1]] = "."
        board_map[next_pos[0]][next_pos[1]] = current_marker
        return board_map

    else:
        current_marker = rotate_guard(current_marker)
        board_map[current_pos[0]][current_pos[1]] = current_marker
        return board_map


def simulate_guard_movement(board_map: List[List[str]]) -> int:
    visited_spots: Set[Tuple[int, int]] = set()
    current_pos = find_guard(board_map)
    visited_spots.add(current_pos)
    next_board = move_guard(board_map, current_pos)
    while next_board is not None:
        current_pos = find_guard(next_board)
        visited_spots.add(current_pos)
        next_board = move_guard(next_board, current_pos)

    return len(visited_spots)


def main():
    input_file = Path(Path(__file__).parent, "input.txt")
    board_map = parse_input(input_file)
    total_visited_spots = simulate_guard_movement(board_map)
    print(total_visited_spots)


if __name__ == "__main__":
    main()
