class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans=[]
        for i,num in enumerate(nums):
            if nums[i]==target:
                ans.append(i)
        return ans
       
