class FreqStack:

    def __init__(self):
        self.stack = []
        self.map_ = defaultdict(lambda:0)
        self.idx = 0
        
    def push(self, val: int) -> None:
        self.map_[val] += 1
        self.idx += 1
        heappush(self.stack,(-self.map_[val],-self.idx,val))
        

    def pop(self) -> int:
        val = heappop(self.stack)
        val = val[2]
        self.map_[val] -= 1
        return val
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
