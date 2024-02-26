class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        stack =[]
        sec = float('-inf')
        if n <=2:
            return False
        for i in range(n-1,-1,-1):
            while stack and nums[i] > stack[-1]:
                x = stack.pop()
                sec = x
            if stack and stack[0] > sec and sec > nums[i]:
                return True
            stack.append(nums[i])

           
        return False