class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            left = 0
            right = len(matrix[i]) - 1

            while left <= right:
                mid = (left + right) // 2
                currentVal = matrix[i][mid]

                if currentVal == target:
                    return True
                elif target < currentVal:
                    right = mid - 1
                else:
                    left = mid + 1
        return False