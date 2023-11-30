class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = l = 0
        r=0
        while r < len(nums):
            r+=1
            if r < len(nums) and nums[l]==nums[r]:
                counter+=1
            else:
                if r==(len(nums)):
                    l+=1
                    r=l
            
        return counter

        