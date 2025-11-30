from typing import Callable, Any


class Area:
    def __init__(self, width: int, height: int, default_value=None):
        self.width = width
        self.height = height
        self.fields = [[default_value] * height for i in range(width)]

    def exists(self, x: int, y: int):
        return not (x < 0 or y < 0 or x >= self.width or y >= self.height)

    def load_from_lines(self, lines: list[str], funct: Callable[[int, int, str], Any] = None):
        for y, line in enumerate(lines):
            line = line.rstrip('\r\n')
            for x, c in enumerate(line):
                if funct:
                    self.set_field(x, y, funct(x, y, c))
                else:
                    self.set_field(x, y, c)

    def for_each(self, funct: Callable[[int, int, Any], Any], start_x: int = 0, start_y: int = 0, end_x: int = None,
                 end_y: int = None):
        if end_x is None:
            end_x = self.width - 1
        if end_y is None:
            end_y = self.height - 1
        for y in range(start_y, end_y + 1):
            for x in range(start_x, end_x + 1):
                funct(x, y, self.fields[x][y])

    def to_string(self) -> str:
        result = ""
        for y in self.fields:
            for x in y:
                result += str(x)
            result += "\n"
        return result

    def set_field(self, x: int, y: int, value: Any):
        self.fields[y][x] = value

    def get_field(self, x: int, y: int):
        return self.fields[y][x]

    def set_region(self, value: Any, start_x: int = 0, start_y: int = 0, end_x: int = None,
                   end_y: int = None):
        if end_x is None:
            end_x = self.width - 1
        if end_y is None:
            end_y = self.height - 1
        for y in range(start_y, end_y + 1):
            for x in range(start_x, end_x + 1):
                self.fields[x][y] = value

    def set_region_dynamic(self, funct: Callable[[int, int, Any], Any], start_x: int = 0, start_y: int = 0,
                           end_x: int = None,
                           end_y: int = None):
        if end_x is None:
            end_x = self.width
        if end_y is None:
            end_y = self.height
        for y in range(start_y, end_y + 1):
            for x in range(start_x, end_x + 1):
                self.fields[x][y] = funct(x, y, self.fields[x][y])
