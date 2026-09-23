class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        mins=0
        fresh=0
        dq=deque()
        directions=[(-1,0),(1,0),(0,1),(0,-1)]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==2:
                    dq.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1
        if fresh==0:
            return 0
        while dq and fresh>0:
            cur_level_fruits=len(dq)
            mins+=1
            for i in range(cur_level_fruits):
                r,c =dq.popleft()
                for dr,dc in directions:
                    nr=r+dr
                    nc=c+dc
                    if nr<0 or nr>=len(grid) or nc<0 or nc>= len(grid[0]):
                        continue
                    #rotten fruit , skip/ empty skip
                    if grid[nr][nc]!=1:
                        continue
                    fresh-=1
                    grid[nr][nc]=2
                    dq.append((nr,nc))
           
        return -1 if fresh>0 else mins
                