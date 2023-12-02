import util


def part_a(lines: list[str]):
    return sum([int(fist_digit(l) + last_digit(l)) for l in lines])


def part_b(lines: list[str]):
    return sum([int(fist_digit_b(l) + last_digit_b(l)) for l in lines])


def fist_digit(text: str) -> str:
    for c in text:
        if c.isdigit():
            return c
    raise Exception()


digit_dict = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
]


def is_digit(text: str):
    for i, v in enumerate(digit_dict):
        if text.startswith(v):
            return str(i + 1)
    return None


def is_digit_last(text: str):
    for i, v in enumerate(digit_dict):
        if text.endswith(v):
            return str(i + 1)
    return None


def fist_digit_b(text: str) -> str:
    for i in range(0, len(text)):
        c = text[i]
        if c.isdigit():
            return c
        c = is_digit(text[i:])
        if c is not None:
            return c

    raise Exception()


def last_digit_b(text: str) -> str:
    for i in range(0, len(text)):
        c = text[len(text) - i - 1]
        if c.isdigit():
            return c
        c = is_digit_last(text[:len(text) - i])
        if c is not None:
            return c

    raise Exception()


def last_digit(text: str) -> str:
    for i in range(0, len(text)):
        if text[len(text) - 1 - i].isdigit():
            return text[len(text) - 1 - i]
    raise Exception()


if __name__ == '__main__':
    print(f'Day 1: part A: {part_a(util.read_file_as_list("data/day1.txt"))}')
    print(f'Day 1: part B: {part_b(util.read_file_as_list("data/day1.txt"))}')
