class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Time - O(n^2)
        #Space - O(1)
        # for m in range(len(matrix)):
        #     for k in range(len(matrix[m])):
        #         if matrix[m][k] == target:
        #             return True
        # return False 

        #optimize time complexity using binary search because increasing matrix.
        #run search per row.

        for row in range(len(matrix)):
            left = 0
            right = len(matrix[row])-1

            while left <= right:
                mid = (left + right)//2
                print(mid)
                current = matrix[row][mid]
                print(" ",current)

                if current == target:
                    return True
                elif current < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False