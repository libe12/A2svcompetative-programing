class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:


        if target not in nums:
            return [-1,-1]

        
        res = []
        l, r = 0, len(nums)
        while l <=r:

            a = (l+r)//2

            if nums[a]>=target:
                ans = a
                r = a-1
            
            else:
                l = a + 1

        sol = 0
        l, r = 0, len(nums)-1 
        while l <=r:
            a = (l+r)//2
            if nums[a] <= target:
                sol = a
                l = a+1
            else:
                r = a-1

        return [ans,sol]
        
 
    