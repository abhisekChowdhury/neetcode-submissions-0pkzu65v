class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            left = 0
            right = len(matrix[row]) - 1

            while left <= right:
                mid = (left + right) // 2
                current_val = matrix[row][mid]
                if target == current_val:
                    return True
                elif target < current_val:
                    right = mid-1
                else:
                    left = mid+1
        return False