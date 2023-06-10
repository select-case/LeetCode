class Solution:
    def trap(self, height: List[int]) -> int:
        pre = [height[0]]
        for i in height:
            if i > pre[-1]: pre.append(i)
            else: pre.append(pre[-1])
        pre.pop(0)
        post = []
        for i in range(len(height)):
            post.append(max(height[i:]))
        print(pre)
        print(post)
        water = 0
        for i in range(len(height)):
            water += min(post[i],pre[i]) - height[i]


        return water

