class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        # code here
        values = [(i.value,i.weight,i.value/i.weight) for i in arr]
        values = sorted(values,key=lambda x: -x[2])
        ans = 0
        for i in range(n):
            if W == 0: ans
            cur_weight = min(W,values[i][1])
            W -= cur_weight
            ans += cur_weight * values[i][2]
            
        return ans
