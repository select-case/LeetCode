class MyQueue:

    def __init__(self):
        self.nums = []

    def push(self, x: int) -> None:
        self.nums.append(x)

    def pop(self) -> int:
        num = self.nums[0]
        self.nums = self.nums[1:]
        return num

    def peek(self) -> int:
        return self.nums[0]

    def empty(self) -> bool:
        return not bool(len(self.nums))


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()