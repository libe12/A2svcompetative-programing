class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        sub =[]

        ans = []

        def backtrack(s):
            if s > len(nums):
                return 
            
            ans.append(sub[:])

            for i in range(s,len(nums)):
                sub.append(nums[i])

                backtrack(i+1)

                sub.pop()
        backtrack(0)

        return ans