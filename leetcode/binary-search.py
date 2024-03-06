class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums)-1

        while l<=r:

            a = (l+r)//2
            if target == nums[a]:
                return a

            elif target > nums[a]:
                l = a+1
            elif target < nums[a]:
                r = a-1
        return -1