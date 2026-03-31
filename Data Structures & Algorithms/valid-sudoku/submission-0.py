class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        column = defaultdict(set)
        box = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                
                box_id = (r//3, c//3)

                if val in row[r] or val in column[c] or val in box[box_id]:
                    return False
                else:
                    row[r].add(val)
                    column[c].add(val)
                    box[box_id].add(val)
                
        return True
                