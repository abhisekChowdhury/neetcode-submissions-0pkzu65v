class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # make three buckets
            # row
                # key - r 
            # column
                # column - c
            # box
                # tuple - (r//3,c//3)

        row = defaultdict(set)
        column = defaultdict(set)
        box = defaultdict(set)

        for r in range(9):
            for c in range(9):

                curr_val = board[r][c]

                if curr_val == ".":
                    continue
                
                box_index = (r//3, c//3)

                if curr_val in row[r] or curr_val in column[c] or curr_val in box[box_index]:
                    return False
                
                row[r].add(curr_val)
                column[c].add(curr_val)
                box[box_index].add(curr_val)
        
        return True