# stack using deque class format
from collections import deque


class Stack:
    def __init__(self):
        self._container = deque()

    def size(self):
        return len(self._container)

    def peek(self):
        if self.size() == 0:
            raise Exception("Stack is empty!")
        return self._container[-1]

    def push(self, item):
        self._container.appendleft(item)

    def pop(self):
        if self.size() == 0:
            raise Exception("Stack is empty!")
        return self._container.popleft()

    def Isempty(self, stack):
        if self.size() == 0:
            print("Isempty() status is True")
        else:
            print("Isempty() status is False")


def __main__():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.size())  # 3
    print(stack.peek())  # 3
    print(stack.pop())  # 3
    print(stack.pop())  # 2
    stack.Isempty(stack)
    print(stack.pop())  # 1


if __name__ == "__main__":
    __main__()
