from util import read_file_as_string, read_file_as_int_list


def part_a(file: str):
    frequencies = read_file_as_int_list(file)
    return sum(frequencies)

def part_b(file: str):
    frequencies = read_file_as_int_list(file)
    current = 0
    previous = set()
    while True:
        for f in frequencies:
            current += f
            if current in previous:
                return current
            previous.add(current)

if __name__ == '__main__':
    print(f'Day 1: part A: {part_a("data/day1.txt")}')
    print(f'Day 1: part B: {part_b("data/day1.txt")}')
