from dataclasses import dataclass
from itertools import product
import math
from pathlib import Path
from typing import Dict, List, Tuple, Set


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


def parse_input(input_file: Path) -> Dict[str, List[Coordinate]]:
    antennas: Dict[str, List[Tuple[int, int]]] = {}
    for i, line in enumerate(input_file.read_text().splitlines()):
        for j in range(len(line)):
            if line[j] != ".":
                antenna = line[j]
                existing_antennas = antennas.get(antenna, [])
                existing_antennas.append(Coordinate(i, j))
                antennas[antenna] = existing_antennas

    return antennas


def find_difference_vector(
    first_antenna: Coordinate, second_antenna: Coordinate
) -> Coordinate:
    return second_antenna - first_antenna


def find_antinodes(
    antenna_locations: List[Coordinate], map_border: Coordinate
) -> Set[Coordinate]:
    antinodes: Set[Coordinate] = set()
    for index, first_location in enumerate(antenna_locations):
        for second_location in antenna_locations[index + 1 :]:
            difference = find_difference_vector(first_location, second_location)
            antinode = first_location
            while 0 <= antinode.x < map_border.x and 0 <= antinode.y < map_border.y:
                antinodes.add(antinode)
                antinode = antinode + difference

            antinode = first_location
            while 0 <= antinode.x < map_border.x and 0 <= antinode.y < map_border.y:
                antinodes.add(antinode)
                antinode = antinode - difference
    return antinodes


def main():
    input_file = Path(Path(__file__).parent, "input.txt")
    num_lines = len(input_file.read_text().splitlines())
    num_columns = len(input_file.read_text().splitlines()[0])

    parsed_input = parse_input(input_file)
    antinodes: Set[Coordinate] = set()

    for antenna_type, antenna_locations in parsed_input.items():
        antinodes.update(
            find_antinodes(antenna_locations, Coordinate(num_lines, num_columns))
        )

    antinodes = list(
        filter(
            lambda coordinate: 0 <= coordinate.x < num_lines
            and 0 <= coordinate.y < num_columns,
            antinodes,
        )
    )
    show_output(input_file, antinodes)
    print(len(antinodes))


def show_output(original_input: Path, output: Set[Coordinate]) -> None:
    text = [list(line) for line in original_input.read_text().splitlines()]
    for antinode in output:
        if 0 <= antinode.x < len(text) and 0 <= antinode.y < len(text[antinode.x]):
            if text[antinode.x][antinode.y] == ".":
                text[antinode.x][antinode.y] = "#"

    output_file = Path(Path(__file__).parent, "output.txt")
    full_text = "\n".join(["".join(line) for line in text])
    output_file.write_text(full_text)


if __name__ == "__main__":
    main()