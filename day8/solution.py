from itertools import product
from pathlib import Path
from typing import Dict, List, Tuple


def parse_input(input_file: Path) -> Dict[str, List[Tuple[int, int]]]:
    antennas: Dict[str, List[Tuple[int, int]]] = {}
    for i, line in enumerate(input_file.read_text().splitlines()):
        for j in range(len(line)):
            if line[j] != ".":
                antenna = line[j]
                existing_antennas = antennas.get(antenna, [])
                existing_antennas.append((i, j))
                antennas[antenna] = existing_antennas

    return antennas


def main():
    input_file = Path(Path(__file__).parent, "input.txt")
    parsed_input = parse_input(input_file)
    print(parsed_input)


if __name__ == "__main__":
    main()
