class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1]*len(nums)
        for i in range(1,len(nums)):
            arr[i] = nums[i-1]*arr[i-1]
        res = [1]*len(nums)
        post = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= post
            post *= nums[i] 
            
        ans = []
        for i in range(len(res)):
            ans.append(arr[i]*res[i])
        return ans
