#########################################################################################################
####     Leetcode 2529. Maximum Count of Positive Integer and Negative Integer     ######################
#########################################################################################################
class Solution:
    def lastNegative(self, nums: List[int]) -> int:
        """
        Function to find the last negative integer close to first occurence of zero

        similar to :
           - First occurence of a number in sorted array
           - Floor of a number in a sorted array
        """
        n = len(nums)
        start = 0
        end = n - 1
        res = -1
        while start <= end:
            mid = start + (end - start)//2
            if nums[mid] >= 0:
                end = mid - 1
            elif nums[mid] < 0:
                res = mid
                start = mid + 1
        return res

    def firstPositive(self, nums: List[int]) -> int:
        """
        Function to find the first positive integer close to last occurence of zero
        
        similar to :
           - Last occurence of a number in sorted array
           - Ceiling of a number in a sorted array
        """
        n = len(nums)
        start = 0
        end = n - 1
        res = -1
        while start <= end:
            mid = start + (end - start)//2
            if nums[mid] <= 0:
                start = mid + 1
            elif nums[mid] > 0:
                res = mid
                end = mid - 1
        return res

    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        last_neg = self.lastNegative(nums)
        first_pos = self.firstPositive(nums)
        num_neg = last_neg + 1 # if last_neg == -1,num_neg is zer0
        num_pos = n - first_pos if first_pos != (-1) else 0
        return max(num_neg,num_pos)