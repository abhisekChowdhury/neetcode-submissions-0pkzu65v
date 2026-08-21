class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in range(len(matrix)):
            for k in range(len(matrix[m])):
                if matrix[m][k] == target:
                    return True
        return False