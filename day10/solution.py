from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import List, Set


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int

    def __add__(self, other: "Coordinate"):
        if type(other) != type(self):
            raise TypeError
        return Coordinate(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Coordinate"):
        if type(other) != type(self):
            raise TypeError
        return Coordinate(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int):
        if type(other) != int:
            raise TypeError
        return Coordinate(other * self.x, other * self.y)


class Direction(Enum):
    NORTH = Coordinate(0, -1)
    WEST = Coordinate(-1, 0)
    EAST = Coordinate(1, 0)
    SOUTH = Coordinate(0, 1)


def parse_input(input_file: Path) -> List[List[int]]:
    return [
        [int(location) for location in line]
        for line in input_file.read_text().splitlines()
    ]


def find_all_trailheads(map: List[List[int]]) -> List[Coordinate]:
    trailheads: List[Coordinate] = list()
    for i, row in enumerate(map):
        for j, position in enumerate(row):
            if position == 0:
                trailheads.append(Coordinate(i, j))

    return trailheads


def find_all_trail_endings_for_trailhead(
    map: List[List[Coordinate]], starting_position: Coordinate
) -> Set[Coordinate]:
    current_value = map[starting_position.x][starting_position.y]
    if current_value == 9:
        return 1

    total_found_trails = 0
    for direction in Direction:
        next_location = starting_position + direction.value
        if 0 <= next_location.x < len(map) and 0 <= next_location.y < len(map[0]):
            next_value = map[next_location.x][next_location.y]
            if next_value != current_value + 1:
                continue
            else:
                total_found_trails += find_all_trail_endings_for_trailhead(
                    map, next_location
                )

    return total_found_trails


def main():
    input_file = Path(Path(__file__).parent, "input.txt")
    parsed_input = parse_input(input_file)
    trailheads = find_all_trailheads(parsed_input)
    total_score = 0
    for trailhead in trailheads:
        found_trails = find_all_trail_endings_for_trailhead(parsed_input, trailhead)
        total_score += found_trails

    print(total_score)


if __name__ == "__main__":
    main()
