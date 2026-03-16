######################################################################################
#########    Leetcode 441. Arranging Coins     #######################################
######################################################################################
class Solution:
    def arrangeCoins(self, n: int) -> int:
        start = 1
        end = n
        res = 0
        while start <= end:
            mid = start + (end - start)//2
            sum = (mid * (mid + 1))//2
            if sum == n:
                return mid
            elif sum < n:
                res = mid
                start = mid + 1
            elif sum > n:
                end = mid - 1
        return res