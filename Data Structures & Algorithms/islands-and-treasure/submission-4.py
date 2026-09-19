class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        dq=deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==0:
                    dq.append((r,c))
        
        while dq:
            r,c= dq.popleft()
            for dr,dc in directions:
                if (r+dr)<0 or (r+dr)>=len(grid) or (c+dc)<0 or (c+dc)>=len(grid[0]):
                    continue
                #water? continue, visited? continue, treasure? continue
                if grid[r+dr][c+dc]!= 2147483647:
                    continue
                grid[r+dr][c+dc]=grid[r][c]+1
                dq.append((r+dr,c+dc))

        
                
     