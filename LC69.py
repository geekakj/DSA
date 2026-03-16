###################################################################################
######   Leetcode 69. Sqrt(x)           ###########################################
###################################################################################
class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Function to find integer square root of x.

        similar to:
        - Floor of a number in a sorted array 
        """
        start = 0
        end = x
        res = -1
        while start <= end:
            mid = start + (end -start)//2
            prod = mid * mid
            if prod == x:
                return mid
            elif prod > x:
                end = mid - 1
            elif prod < x:
                res = mid
                start = mid + 1
        return res