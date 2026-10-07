class MinStack:
    def __init__(self):
        self.stack = []
        self.min = 2 ** 31 - 1

    def push(self, value: int) -> None:
        self.stack.append(value)
        self.min = min(self.min, value)

    def pop(self) -> None:
        self.stack.pop(-1)
        if self.stack:
            self.min = min(self.stack)
        else:
            self.min = 2 ** 31 - 1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min