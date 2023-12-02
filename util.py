def read_file_as_list(path_to_file) -> list[str]:
    with open(path_to_file) as f:
        return f.readlines()


def read_file_as_int_list(path_to_file) -> list[int]:
    return [int(x) for x in read_file_as_list(path_to_file)]


def read_file_as_string(path_to_file) -> str:
    result: str = ""
    with open(path_to_file) as f:
        for line in f.readline():
            result += line
    return result


class Vector2d:
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def move(self, move_by):
        return Vector2d(self.x + move_by.x, self.y + move_by.y)


VECTOR_NORTH = Vector2d(0, -1)
VECTOR_SOUTH = Vector2d(0, 1)
VECTOR_WEST = Vector2d(-1, 0)
VECTOR_EAST = Vector2d(1, 0)
