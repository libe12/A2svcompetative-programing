class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        d={0:0,1:0}
        l = 0
        ans = 0
        for i in range(len(nums)):
            d[nums[i]]+=1 
            while d[0]>k:
                d[nums[l]]-=1
                l+=1
            ans = max(ans,i-l+1)
        return ans
        