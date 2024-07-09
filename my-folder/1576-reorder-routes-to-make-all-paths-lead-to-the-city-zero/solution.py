class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))
        print(graph)
        
        def dfs(node, parent):
            count = 0
            for n,d in graph[node]:
                if n != parent:
                    count += d
                    count += dfs(n, node)
            return count
        return dfs(0,-1)
        

