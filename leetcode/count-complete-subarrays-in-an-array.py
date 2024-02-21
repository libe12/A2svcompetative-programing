class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        len_ch = len(set(nums))
        n = len(nums)
        
        counter = 0
        for i in range(n):
            s = set()
            for j in range(i,n):
                s.add(nums[j])
                if len(s)== len_ch:
                    counter += 1
        return counter
        