#########################################################################################
#####    Leetcode 240. Search a 2D Matrix II                 ############################
#########################################################################################
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)  # no of rows
        n = len(matrix[0])  # no of columns
        i = 0
        j = n - 1
        while j >= 0 and i < m:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
        return False