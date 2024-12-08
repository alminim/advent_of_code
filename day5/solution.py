from pathlib import Path
from typing import List, Tuple


ORDER: List[Tuple[str, str]] = list()


def parse_input(input_file: Path) -> List[str]:
    return input_file.read_text().splitlines()


def create_order(order_rules: List[str]) -> None:
    for rule in order_rules:
        ORDER.append(tuple(rule.split("|")))


def check_update_matches_order(update: str) -> bool:
    update_pages = update.split(",")
    return all(
        (update_pages[i], update_pages[i + 1]) in ORDER
        for i in range(len(update_pages) - 1)
    )


def main():
    input_file = Path(Path(__file__).parent, "input.txt")
    instructions = parse_input(input_file)
    ordering_rules = instructions[: instructions.index("")]
    update_rules = instructions[instructions.index("") + 1 :]
    create_order(ordering_rules)

    correct_updates = [
        update for update in update_rules if check_update_matches_order(update)
    ]
    print(
        sum(
            int(update.split(",")[len(update.split(",")) // 2])
            for update in correct_updates
        )
    )


if __name__ == "__main__":
    main()
