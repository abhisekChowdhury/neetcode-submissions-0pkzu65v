class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        for row in range(rows):
            left = 0
            right = cols-1

            while left <= right:
                mid = (left + right) // 2
                current = matrix[row][mid]
                if current == target:
                    return True
                elif current < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False