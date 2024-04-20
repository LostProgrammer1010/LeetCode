class MyQueue:

    def __init__(self):
        self.stack = List()

    def push(self, x: int) -> None:
        self.stack.insert(0, x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        return -1

    def peek(self) -> int:
        return self.stack[len(self.stack)-1]

    def empty(self) -> bool:
        return not self.stack

