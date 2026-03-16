##############################################################################
#####   Leetcode 367. Valid Perfect Square    ################################
##############################################################################
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = 1
        end = num
        while start <= end:
            mid = start + (end - start)//2
            prod = mid * mid
            if prod == num:
                return True
            elif prod > num:
                end = mid - 1
            elif prod < num:
                start = mid + 1
        return False