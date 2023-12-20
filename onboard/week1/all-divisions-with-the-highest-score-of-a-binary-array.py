class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        l = i = 0
        r = sum(nums)
        arr = [r]
        while i < len(nums):
            if nums[i]==0:
                l +=1
            elif nums[i]==1:
                r -= 1
            arr.append(l+r)
            i += 1
        max_val = max(arr)
        res = []
        for i, num in enumerate(arr):
            if num == max_val:
                res.append(i)
        return res
        
        


        