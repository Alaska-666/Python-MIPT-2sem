import sys


class ExtendedList(list):
    @property
    def reversed(self):
        return list(reversed(self))

    @property
    def first(self):
        return self[0]

    @first.setter
    def first(self, value):
        self[0] = value

    @property
    def last(self):
        return self[len(self) - 1]

    @last.setter
    def last(self, value):
        self[len(self) - 1] = value

    @property
    def size(self):
        return len(self)

    @size.setter
    def size(self, value):
        if value > len(self):
            for i in range(0, value - len(self), 1):
                self.append(None)
        elif value < len(self):
            for i in range(0, len(self) - value, 1):
                self.pop()

    F = first
    R = reversed
    L = last
    S = size
exec(sys.stdin.read())
