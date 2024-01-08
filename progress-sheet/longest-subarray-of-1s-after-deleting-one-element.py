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
            ans = max(ans,d[1])
        
        for num in nums:
            if num!=0:
                continue
            else:return ans
        return ans-1