class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = '{0:032b}'.format(start)
        goal = '{0:032b}'.format(goal)
        count = 0
        for i in range(len(start)):
            if start[i] != goal[i]:
                count += 1
        return count

