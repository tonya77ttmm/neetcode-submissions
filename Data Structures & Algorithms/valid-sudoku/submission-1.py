class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_seen=[set() for _ in range(9)]
        columns_seen=[set() for _ in range(9)]
        sub_boxes_seen=[set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                if board[i][j] in rows_seen[i]:
                    return False
                rows_seen[i].add(board[i][j])
                if board[i][j] in columns_seen[j]:
                    return False
                columns_seen[j].add(board[i][j])
                #sub box
                # 0 1 2\3,4,5\6,7,8
                #i/3=0-2
                #j/3=0-2
                #i/3*3+j/3 
                index=i//3*3+j//3
                if board[i][j] in sub_boxes_seen[index]:
                    return False
                sub_boxes_seen[index].add(board[i][j])
        return True