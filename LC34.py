#################################################################################################
########  Leetcode 34. Find First and Last Position of Element in Sorted Array    ###############
#################################################################################################
class Solution:
    def firstOccurence(self,nums: List[int], target: int) -> int:
        n = len(nums)
        start = 0
        end = n - 1
        res = -1
        while start <= end:
            mid = start + (end -start)//2
            if nums[mid] == target:
                res = mid
                end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
        return res

    def lastOccurence(self,nums: List[int], target: int) -> int:
        n = len(nums)
        start = 0
        end = n - 1
        res = -1
        while start <= end:
            mid = start + (end -start)//2
            if nums[mid] == target:
                res = mid
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
        return res

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = list()
        res.append(self.firstOccurence(nums,target))
        res.append(self.lastOccurence(nums,target))
        return res