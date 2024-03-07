class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            if currSum > maxi:
                maxi = currSum
            if currSum < 0:
                currSum = 0
        return maxi