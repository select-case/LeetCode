class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        nums = [num1, num2, num3]
        for i in range(len(nums)):
            if nums[i] < 10:
                nums[i] = "000" + str(nums[i])
            elif nums[i] < 100:
                nums[i] = "00" + str(nums[i])
            elif nums[i] < 1000:
                nums[i] = "0" + str(nums[i])
            else:
                nums[i] = str(nums[i])
        
        ans = []
        print(nums)
        for i in range(4):
            ans.append(min(int(nums[0][i]),int(nums[1][i]),int(nums[2][i])))
            ans[-1] = str(ans[-1])
        print(ans)
        ret =  "".join(ans)
        return int(ret)
