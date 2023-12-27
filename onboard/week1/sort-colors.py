class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i,num in enumerate(nums):
            res = min(nums[i:])
            l = nums.index(res)
            nums[i],nums[l] = nums[l],nums[i]
        if nums == nums.sort():
            return nums
        else:
            return reversed(nums)

        """
        Do not return anything, modify nums in-place instead.
        """
        