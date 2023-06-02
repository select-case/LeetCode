import math
class Solution:
    def dfs(self,adj_list,visited,c,i):
        visited[i] = True
        c[0] += 1
        for j in adj_list[i]:
            if not visited[j]:
                self.dfs(adj_list, visited,c,j)


    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj_list = {}
        for i in range(len(bombs)):
            adj_list[i] = []
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j:
                    p = [bombs[i][0],bombs[i][1]]
                    q = [bombs[j][0],bombs[j][1]]

                    distance = math.dist(p,q)
                    if distance <= bombs[i][2]:
                        adj_list[i].append(j)
        print(adj_list)

        ans = -1
        for i in range(len(bombs)):
            c = [0]
            visited = [False] * len(bombs)
            self.dfs(adj_list, visited, c ,i)
            ans = max(ans,c[0])
        
        return ans