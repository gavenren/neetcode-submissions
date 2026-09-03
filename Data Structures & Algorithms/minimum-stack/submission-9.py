class MinStack:

    def __init__(self):
        self.stack = []
        self.count = {}

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.count[val] = 1 + self.count.get(val, 0)
    def pop(self) -> None:
        if self.count[self.stack[-1]] == 1:
            del self.count[self.stack[-1]]
        else:
            self.count[self.stack[-1]] -= 1
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.count:
            return min(self.count)
