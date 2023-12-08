class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l = 0
        r = 1
        res =[]
        while r < len(nums):
            for _ in range(nums[l]):
                res.append(nums[r])
            l = r+1
            r = l+1
        return res
        