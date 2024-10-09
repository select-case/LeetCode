class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0
        for i in s:
            if i == ")" and len(stack) == 0:
                count += 1
            elif i == ")":
                stack = stack[:-1]
            else: 
                stack.append(i)
        return count + len(stack)
