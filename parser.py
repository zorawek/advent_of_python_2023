from typing import Self


class Parsable:
    def __init__(self, text: str):
        super().__init__()
        self.text = text
        self.index = 0

    def eat_tokens(self, values: list[str]):
        for v in values:
            if self.text[self.index:].startswith(v):
                self.index += len(v)
                return v
        raise Exception(f"Could not find any tokens {values}")

    def eat_token(self, value: str):
        if self.text[self.index:].startswith(value):
            self.index += len(value)
            return value
        raise Exception(f"Could not find token {value}")

    def has_token(self, value: str):
        return self.text[self.index:].startswith(value)

    def has_int(self):
        result = ""
        for i in range(self.index, len(self.text)):
            c = self.text[i]
            if c.isdigit():
                result += c
            else:
                break
        return len(result) > 0

    def has_text(self):
        result = ""
        for i in range(self.index, len(self.text)):
            c = self.text[i]
            if c != " ":
                result += c
            else:
                break
        return len(result) > 0

    def eat_int(self):
        result = ""
        negative = False
        for i in range(self.index, len(self.text)):
            c = self.text[i]
            if c.isdigit():
                result += c
            elif c == '-' and i == self.index:
                negative = True
            else:
                break
        if len(result) > 0:
            self.index += len(result)
            if negative:
                self.index += 1
            return -int(result) if negative else int(result)
        raise Exception(f"Could not find integer")

    def eat_string(self, delimiter=None):
        if delimiter is None:
            delimiter = [" ", "\n"]
        result = ""
        for i in range(self.index, len(self.text)):
            c = self.text[i]
            if c not in delimiter:
                result += c
            else:
                break
        if len(result) > 0:
            self.index += len(result)
            return result
        raise Exception(f"Could not find any string")

    def ignore_token(self, value: str) -> Self:
        if self.text[self.index:].startswith(value):
            self.index += len(value)
            return self
        raise Exception(f"Could not find token {value}. Found: {self.text[self.index:]}")

    def ignore_spaces(self) -> Self:
        for i in range(self.index, len(self.text)):
            c = self.text[i]
            if c == ' ':
                self.index = i + 1
            else:
                break
        return self
