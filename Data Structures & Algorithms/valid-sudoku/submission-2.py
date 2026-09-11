class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        for r in range(9):
            for c in range(9):

                current_value = board[r][c]

                if current_value == ".":
                    continue
                
                box_index = (r//3, c//3)

                if current_value in row[r] or current_value in col[c] or current_value in box[box_index]:
                    return False
                
                row[r].add(current_value)
                col[c].add(current_value)
                box[box_index].add(current_value)
        
        return True