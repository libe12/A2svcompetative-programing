class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        mod = 10**9 +7
        n = len(nums)
        left = [0]* n
        stk = []
        right = [n-1]*n
        for i in range(n):
            
            while stk and nums[i] < nums[stk[-1]]:
                j = stk.pop()
                right[j] = i-1
                
            
            if stk:
                left[i] = stk[-1]+1
            stk.append(i)
        ans = 0
        for i in range(n):
            l = i - left[i] + 1
            r = right[i] - i + 1
            ans  += l*r*nums[i]
        return ans % mod

        