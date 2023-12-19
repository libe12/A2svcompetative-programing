class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = list(range(n)) 
        p = 0
        while len(nums) > 1:
            p = (p+k-1)%len(nums)
            nums.pop(p)
        return nums[0]+1
            

        