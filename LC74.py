###########################################################################################
###########   Leetcode 74. Search a 2D Matrix     #########################################
###########################################################################################
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)  # no of rows
        n = len(matrix[0]) # no of columns
        start = 0
        end = (m * n) - 1
        i = 0
        j = 0
        while start <= end and i < m and j < n:
            mid = start + (end - start)//2
            i = mid // n
            j = mid % n
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                end = mid - 1
            elif matrix[i][j] < target:
                start = mid + 1
        return False