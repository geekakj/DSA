####################################################################################################
######   Leetcode 744. Find Smallest Letter Greater Than Target    #################################
####################################################################################################
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if(letters[0] > target) or (letters[-1] <= target):
            return letters[0]
        
        n = len(letters)
        start = 0
        end = n - 1
        res = -1
        while start <= end:
            mid = start + (end - start)//2
            if letters[mid] <= target:
                start = mid + 1
            elif letters[mid] > target:
                res = mid
                end = mid - 1
        return letters[res]