class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        s = set(nums)
        r = 0
        for num in nums:
            if num in s:
                s.remove(num)
                if s:
                    r += len(s)
            else:
                if s:r += len(s)
        return r

      

        