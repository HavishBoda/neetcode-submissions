class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in cols[j] and board[i][j]:
                    cols[j].add(board[i][j])
                else:
                    return False
                if board[i][j] not in boxes[(i//3)*3 + (j//3)]:
                    boxes[(i//3)*3 + (j//3)].add(board[i][j])
                else:
                    return False
                if board[i][j] not in rows[i]:
                    rows[i].add(board[i][j])
                else:
                    return False
        
        return True
