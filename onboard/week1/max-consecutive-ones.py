class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = r = 0  
        res = 0
        while r<len(nums):
            if  nums[r]==0:
                r=r+1
                l=r
            else:
                r+=1
            res=max(res,r-l)
        return res
        