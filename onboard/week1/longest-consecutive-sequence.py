class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_num = set(nums)
        max_val = 0
        for num in nums:
            if num - 1 not in set_num:
                nextnum = num +1
                while nextnum in set_num:
                    nextnum += 1
                max_val = max(max_val, nextnum - num)
        return max_val