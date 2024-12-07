from pathlib import Path
from typing import List, Tuple


WORD_TO_FIND = "XMAS"


def parse_input(input_file: Path) -> List[str]:
    return input_file.read_text().splitlines()


def rotate_text_block(text_block: List[str]) -> List[str]:
    """
    Rotates text 90 degrees clockwise:
    AB becomes CA
    CD         DB
    """
    return [
        "".join(text_block[-1 - i][j] for i in range(len(text_block)))
        for j in range(len(text_block[0]))
    ]


def diagonalise_text_block(text_block: List[str]) -> List[str]:
    diagonalised_text: List[str] = list()
    for i in range(len(text_block)):
        diagonalised_text.append(
            "".join(text_block[i + j][j] for j in range(len(text_block[0]) - i))
        )

    for i in range(1, len(text_block[0])):
        diagonalised_text.append(
            "".join(text_block[j][i + j] for j in range(len(text_block[0]) - i))
        )
    return diagonalised_text


def count_words(text_block: List[str]) -> int:
    total_words = 0
    for line in text_block:
        total_words += line.count(WORD_TO_FIND)

    return total_words


def get_subblock(
    text_block: List[str], center: Tuple[int, int], size: int
) -> List[str]:
    subblock: List[str] = list()
    for line in text_block[center[0] - size // 2 : center[0] + size // 2 + 1]:
        subblock.append(line[center[1] - size // 2 : center[1] + size // 2 + 1])

    return subblock


def check_xmas(input_block: List[str]) -> bool:
    total_mas = 0
    for _ in range(4):
        total_mas += diagonalise_text_block(input_block).count("MAS")
        input_block = rotate_text_block(input_block)

    return total_mas == 2


def count_xmas(text_block: List[str]) -> int:
    total_xmas = 0
    for i in range(1, len(text_block) - 1):
        for j in range(1, len(text_block[i]) - 1):
            if text_block[i][j] == "A":
                subblock = get_subblock(text_block, (i, j), 3)
                if check_xmas(subblock):
                    total_xmas += 1

    return total_xmas


def main():
    input_file = Path(Path(__file__).parent, "input.txt")
    input_block = parse_input(input_file)

    print(count_xmas(input_block))
    # total_words = 0
    # for _ in range(4):
    #     rotated_text = rotate_text_block(input_block)
    #     diagonalised_text = diagonalise_text_block(input_block)

    #     total_words += count_words(rotated_text)
    #     total_words += count_words(diagonalised_text)

    #     input_block = rotated_text


if __name__ == "__main__":
    main()
