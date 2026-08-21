class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS=len(board) #3
        COLS=len(board[0])

        def dfs(row,col,index):
            if index==len(word):
                return True
            if row<0 or row>=ROWS or col<0 or col>=COLS or board[row][col]!=word[index]:
                return False
            #mark as visited(
            temp=board[row][col]
            board[row][col]='#'
            for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                if dfs(row+dr,col+dc,index+1):
                    return True
            board[row][col]=temp
            return False
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]==word[0] and dfs(r,c,0):
                    return True
        return False