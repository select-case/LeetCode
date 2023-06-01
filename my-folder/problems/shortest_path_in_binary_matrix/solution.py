class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ans=0
        m=len(grid)
        n=len(grid[0])
        if grid[0][0]==1 or grid[m-1][n-1]==1:
            return -1

        q=[(0,0)]
        while q:
            q2=[]
            ans+=1

            while q:
                x,y=q.pop()
                if(x,y)==(m-1,n-1):
                    return ans

                for i,j in(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1):
                    x2,y2=x+i,y+j

                    if 0<=x2<m and 0<=y2<n and not grid[x2][y2]:
                        grid[x2][y2]=1

                        q2.append((x2,y2))

            q=q2

        return -1                            