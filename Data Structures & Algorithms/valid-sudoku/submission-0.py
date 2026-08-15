class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            stt = set()
            for j in range(len(board[0])):
                if board[i][j] == "." :
                    continue
                if board[i][j] in stt:
                    return False
                stt.add(board[i][j])

        for i in range(len(board[0])):
            stt = set()
            for j in range(len(board)):
                if board[j][i] == "." :
                    continue
                if board[j][i] in stt:
                    return False
                stt.add(board[j][i])

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                stt = set()
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        if board[k][l] == "." :
                            continue
                        if board[k][l] in stt:
                            return False
                        stt.add(board[k][l])

        return True
