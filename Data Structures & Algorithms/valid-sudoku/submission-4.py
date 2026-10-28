class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        for r in range(9):
            for c in range(9):
                current = board[r][c]

                if current == ".":
                    continue

                box_id = (r//3,c//3)
                
                if current in row[r] or current in col[c] or current in box[box_id]:
                    return False
                
                row[r].add(current)
                col[c].add(current)
                box[box_id].add(current)
        
        return True
