class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj_lst = {}
        for i in range(len(isConnected)):
            adj_lst[i] = []
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    adj_lst[i].append(j)
        visited = [False for i in range(len(isConnected))]
        provinces = 0
        while False in visited:
            start = 0
            provinces += 1
            for i in range(len(visited)):
                if visited[i] == False:
                    start = i
                    break
            to_explore = [start]
            while to_explore:
                cur = to_explore.pop()
                visited[cur] = True
                for i in adj_lst[cur]:
                    if visited[i] == False:
                        to_explore.append(i)
            
        return provinces