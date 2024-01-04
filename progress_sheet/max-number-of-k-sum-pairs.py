class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        operation = 0
        l, r = 0, len(nums)-1
        while r > l:
            if nums[r] + nums[l] == k:
                operation += 1
                l += 1
                r -= 1
            if nums[r] + nums[l] > k:
                r -= 1

            if nums[r] + nums[l] < k:

                l += 1
        return operation
        