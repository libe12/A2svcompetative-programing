class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #nums.sort()
        l = 0
        ans = 0
        res = float('inf')
        for r in range(len(nums)):
            if nums[r]==target:
                return 1
            else:
                ans += nums[r]
                while ans >= target:
                    res = min (res,r-l+1)
                    ans-=nums[l]
                    l+=1
        return res if res != float('inf') else 0
        