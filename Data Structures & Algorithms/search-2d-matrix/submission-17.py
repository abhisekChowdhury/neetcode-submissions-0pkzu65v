class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        row_left, row_right = 0, rows-1
        while row_left <= row_right:
            mid_row = (row_left + row_right) // 2
            if matrix[mid_row][0] == target:
                return True
            elif matrix[mid_row][0] < target:
                row_left = mid_row + 1
            else:
                row_right = mid_row - 1

            left, right = 0, cols-1

            while left <= right:
                mid = (left + right) // 2

                if matrix[mid_row][mid] == target:
                    return True
                elif matrix[mid_row][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

        return False