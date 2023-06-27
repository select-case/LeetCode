import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        li =  [(-nums[i],i) for i in range(k)]
        heapq.heapify(li)
        ans = []
        smallest = heappop(li)
        heappush(li, smallest)
        ans.append(-smallest[0])
        for i in range(k,len(nums)):
            heapq.heappush(li,(-nums[i],i))
            while li[0][1] <= i-k:
                heapq.heappop(li)
            smallest = heappop(li)
            heappush(li, smallest)
            ans.append(-smallest[0])
        

        return ans