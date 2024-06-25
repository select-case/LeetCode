class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj_list = {}
        for i in range(len(manager)):
            adj_list[i] = []
        for i in range(len(manager)):
            if i != headID:
                adj_list[manager[i]].append(i)
        q = [headID]
        ans_lst = [0 for i in range(n)]
        while q:
            cur = q.pop()
            for i in adj_list[cur]:
                ans_lst[i] = ans_lst[cur] + informTime[cur]
            q += adj_list[cur]
        return max(ans_lst)
