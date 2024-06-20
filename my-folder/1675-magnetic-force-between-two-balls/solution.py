class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        r = (position[-1] - position[0])//((m-1))
        l = 1
        while l <= r:
            mid = l + (r - l) // 2
            last = position[0]
            balls = 1
            print("L:",l," r:",r," m:",mid)
            for i in range(1,len(position)):
                if position[i] - last >= mid:
                    last = position[i]
                    balls += 1
            print("balls",balls)
            if balls >= m:
                ans = mid
                l = mid + 1
            else: r = mid - 1
        return ans

