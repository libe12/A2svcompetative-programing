class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = []
        l = sorted(nums)
        for num in nums:
            arr.append(l.index(num))
        return arr




        