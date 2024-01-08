class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        d = {0:0,1:0}
        l = 0
        ans = 0

        for r in range(len(nums)):
            while d[0] > 1:
                d[nums[l]]-=1
                l+=1
            d[nums[r]]+=1
            if d[0] > 0:
                ans = max(ans,d[1])
            else:
                ans = max(ans, d[1]-1)
        return ans
        
        