class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n):
            l, r = 0, i-1
            while r>l:
                if nums[r] + nums[l] > nums[i]:
                    ans += r-l
                    r -= 1
                else:
                    l += 1
        return ans


        