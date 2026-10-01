class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # border_O=set()
        ROWS,COLS=len(board),len(board[0])
        directions=[(-1,0),(1,0),(0,-1),(0,1)]

        def dfs(r,c): #mark all Os connected to borderOs as #
            if r<0 or r==ROWS or c<0 or c==COLS or board[r][c]=='X' or board[r][c]=='#':
                return
            board[r][c]='#'
            for dr,dc in directions:
                dfs(r+dr,c+dc)

            
        for c in range(COLS):
            dfs(0,c)
            dfs(ROWS-1,c)
        for r in range(ROWS):
            dfs(r,0)
            dfs(r,COLS-1)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=='O':
                    board[r][c]='X'
                elif board[r][c]=='#':
                    board[r][c]='O'
        