from pathlib import Path
from typing import List


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


def main():
    input_file = Path(Path(__file__).parent, "input.txt")
    input_block = parse_input(input_file)

    total_words = 0
    for _ in range(4):
        rotated_text = rotate_text_block(input_block)
        diagonalised_text = diagonalise_text_block(input_block)

        total_words += count_words(rotated_text)
        total_words += count_words(diagonalised_text)

        input_block = rotated_text

    print(total_words)


if __name__ == "__main__":
    main()
