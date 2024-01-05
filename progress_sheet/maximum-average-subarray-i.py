class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum=0
        for i in range(0,k):
            current_sum=current_sum+nums[i]
        
        
        l, r=0, k
        max_val=current_sum
        while r<len(nums):
            current_sum=current_sum-nums[l]+nums[r]
            max_val=max(max_val, current_sum)
            l+=1
            r+=1
            
        return max_val/k


        