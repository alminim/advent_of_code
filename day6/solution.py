from pathlib import Path
from typing import List, Set, Tuple

GUARD_ROTATE_ORDER = ["^", ">", "v", "<"]

GUARD_MOVE_DIRECTION = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def parse_input(input_file: Path) -> List[List[str]]:
    return [list(line) for line in input_file.read_text().splitlines()]


def copy_board(board_map: List[List[str]]) -> List[List[str]]:
    new_board = []
    for row in board_map:
        new_board.append(row.copy())
    return new_board


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

    if (next_pos[0] >= len(board_map) or next_pos[1] >= len(board_map[0])) or (
        next_pos[0] < 0 or next_pos[1] < 0
    ):
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


def add_obstacle(board_map: List[List[str]], obstacle_position: Tuple[int, int]):
    board_map[obstacle_position[0]][obstacle_position[1]] = "O"
    return board_map


def check_repeats_in_simulation(board_map: List[List[str]]) -> bool:
    visited_spots: Set[Tuple[int, int, str]] = set()
    current_pos = find_guard(board_map)
    visited_spots.add(
        (current_pos[0], current_pos[1], board_map[current_pos[0]][current_pos[1]])
    )
    next_board = move_guard(board_map, current_pos)
    while next_board is not None:
        current_pos = find_guard(next_board)
        current_marker = next_board[current_pos[0]][current_pos[1]]
        if (current_pos[0], current_pos[1], current_marker) in visited_spots:
            return True
        visited_spots.add(
            (current_pos[0], current_pos[1], board_map[current_pos[0]][current_pos[1]])
        )
        next_board = move_guard(next_board, current_pos)
    return False


def simulate_guard_movement(board_map: List[List[str]]) -> Set[Tuple[int, int]]:
    visited_spots: Set[Tuple[int, int]] = set()
    original_pos = find_guard(board_map)
    visited_spots.add(original_pos)
    next_board = move_guard(board_map, original_pos)
    while next_board is not None:
        current_pos = find_guard(next_board)
        visited_spots.add(current_pos)
        next_board = move_guard(next_board, current_pos)

    visited_spots.remove(original_pos)
    return visited_spots


def main():
    input_file = Path(Path(__file__).parent, "input.txt")
    board_map = parse_input(input_file)
    visited_spots = simulate_guard_movement(copy_board(board_map))
    total_obstacles_to_add = 0
    for visited_spot in visited_spots:
        new_board = add_obstacle(copy_board(board_map), visited_spot)
        if check_repeats_in_simulation(new_board):
            total_obstacles_to_add += 1

    print(total_obstacles_to_add)


if __name__ == "__main__":
    main()
