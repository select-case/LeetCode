class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visited[i][j]:
                    count += 1
                    lst = [(i,j)]
                    while lst:
                        x,y = lst.pop(0)
                        if not visited[x][y]:
                            visited[x][y] = True
                            if x >= 1:
                                if grid[x-1][y] == "1" and not visited[x-1][y]:
                                    lst.append((x-1,y))
                            if x < len(grid) - 1:
                                if grid[x+1][y]== "1" and not visited[x+1][y]:
                                    lst.append((x+1,y))
                            if y >= 1:
                                if grid[x][y-1]== "1" and not visited[x][y-1]:
                                    lst.append((x,y-1))
                            if y < len(grid[0]) - 1:
                                if grid[x][y+1]== "1" and not visited[x][y+1]:
                                    lst.append((x,y+1))
                            print(lst)
        return count
                                
                            
