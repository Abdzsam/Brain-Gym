class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def noDupRow(Boardrow):
            hshmp = {}
            for i in range(len(Boardrow)):
                if Boardrow[i] == '.':
                    continue
                if Boardrow[i] not in hshmp:
                    hshmp[Boardrow[i]] = i
                else:
                    return False
            return True

        def noDupCol(idxCol):
            hshmp = {}
            for j in range(9):
                if board[j][idxCol] == '.':
                    continue
                if board[j][idxCol] not in hshmp:
                    hshmp[board[j][idxCol]] = j
                else:
                    return False
            return True

        def noDupBox(startRow, startCol):
            hshmp = {}
            for i in range(startRow, startRow + 3):
                for j in range(startCol, startCol + 3):
                    if board[i][j] == '.':
                        continue
                    if board[i][j] not in hshmp:
                        hshmp[board[i][j]] = 1
                    else:
                        return False
            return True

        for i in range(9):
            if not noDupRow(board[i]):
                return False

        for i in range(9):
            if not noDupCol(i):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not noDupBox(i, j):
                    return False

        return True