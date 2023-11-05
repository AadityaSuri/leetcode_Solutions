class MinStack:

    def __init__(self):
        self.ele_stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.ele_stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.ele_stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.ele_stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]