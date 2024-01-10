class Solution:
    def sortColors(self, nums: List[int]) -> None:

        for i in range(1,len(nums)):
            l = i
            while l >0:
                if nums[l-1] > nums[l]:
                    nums[l-1],nums[l]=nums[l],nums[l-1]
                l-=1

        return nums
        """
        Do not return anything, modify nums in-place instead.
        """
        