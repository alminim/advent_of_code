from pathlib import Path
from typing import List, Tuple


ORDER: List[Tuple[str, str]] = list()


def parse_input(input_file: Path) -> List[str]:
    return input_file.read_text().splitlines()


def create_order(order_rules: List[str]) -> None:
    for rule in order_rules:
        ORDER.append(tuple(rule.split("|")))


def create_all_pairs(update: str) -> List[Tuple[str, str]]:
    pages = update.split(",")
    pairs: List[Tuple[str, str]] = list()
    for i in range(len(pages)):
        for j in range(i, len(pages)):
            pairs.append((pages[i], pages[j]))

    return pairs


def check_update_matches_order(update: str) -> bool:
    update_pairs = create_all_pairs(update)
    for pair in update_pairs:
        if (pair[1], pair[0]) in ORDER:
            return False

    return True


def main():
    input_file = Path(Path(__file__).parent, "input.txt")
    instructions = parse_input(input_file)
    ordering_rules = instructions[: instructions.index("")]
    update_rules = instructions[instructions.index("") + 1 :]
    create_order(ordering_rules)
    for update in update_rules:
        print(check_update_matches_order(update))


if __name__ == "__main__":
    main()
