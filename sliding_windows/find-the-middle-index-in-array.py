class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        arr = [0]
       
        for i in range(1,n):
            nums[i] += nums[i-1]
        num = arr + nums
    
        for i in range(1, len(num)):
            if num[-1] - num[i] == num[i-1]:
                return i-1
            #if nums[n-2] == 0:
                #return n-1
        return -1

        