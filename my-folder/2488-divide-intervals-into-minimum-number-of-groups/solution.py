class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start_times = sorted(i[0] for i in intervals)
        end_times = sorted(i[1] for i in intervals)
        ptr, count = 0, 0

        for i in start_times:
            if i > end_times[ptr]:
                ptr += 1
            else:
                count += 1
        
        return count
