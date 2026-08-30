class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        for row in range(rows):
            left, right = 0, len(matrix[row])-1
            while left <= right:
                mid = (left + right) // 2
                current = matrix[row][mid]
                if current == target:
                    return True
                elif current < target:
                    left += 1
                else:
                    right -= 1
        return False