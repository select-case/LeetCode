class Solution:
	def subsetSums(self, arr, n):
		# code here
		ans = []
        def subsetSumsHelper(ind: int, sum: int):
            if ind == n:
                ans.append(sum)
                return
            # element is picked
            subsetSumsHelper(ind + 1, sum + arr[ind])
            # element is not picked
            subsetSumsHelper(ind + 1, sum)
        subsetSumsHelper(0, 0)
        ans.sort()
        return ans
