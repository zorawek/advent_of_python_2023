import parser
import util


#     Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
def parse_line(line: str):
    result = dict()
    p = parser.Parsable(line)
    p.ignore_token("Game ")
    game_id = p.eat_int()
    p.ignore_token(": ")
    while True:
        p.ignore_spaces()
        count = p.eat_int()
        p.ignore_spaces()
        color = p.eat_string(delimiter=[",", ";", "\n"])

        if color in result:
            if result[color] < count:
                result[color] = count
        else:
            result[color] = count

        if p.has_token(","):
            p.eat_token(",")
            continue
        if p.has_token(";"):
            p.eat_token(";")
            continue
        break
    return game_id, result


def is_possible(game, filter):
    for k, v in game.items():
        if k in filter:
            if filter[k] < v:
                return False
        else:
            return False
    return True


def part_a(lines: list[str]):
    result = 0
    filter = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    for l in lines:
        game_id, values = parse_line(l)

        if is_possible(values, filter):
            result += game_id
    return result


def part_b(lines: list[str]):
    result = 0
    for l in lines:
        game_id, values = parse_line(l)
        game_value = 1
        for v in values.values():
            game_value *= v
        result += game_value
    return result


if __name__ == '__main__':
    print(f'Day 2: part A: {part_a(util.read_file_as_list("data/day2.txt"))}')
    print(f'Day 2: part B: {part_b(util.read_file_as_list("data/day2.txt"))}')
