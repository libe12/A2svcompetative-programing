class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ans = []
        
        perm = []
        def backtrack(s):

            if len(perm) == len(nums) and sorted(perm[:])==nums:
                ans.append(perm[:])
                return

            elif len(perm) == len(nums) and sorted(perm[:])!=nums:
                return

            for i in range(0,len(nums)):
                perm.append(nums[i])
                backtrack(i+1)
                perm.pop()

        backtrack(0)

        return ans




        