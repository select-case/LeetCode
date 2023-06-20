class MyStack:

    def __init__(self):
        self.nums = []

    def push(self, x: int) -> None:
        self.nums.append(x)

    def pop(self) -> int:
        num = self.nums[-1]
        self.nums = self.nums[:-1]
        return num

    def top(self) -> int:
        return self.nums[-1]

    def empty(self) -> bool:
        return not bool(len(self.nums))


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()