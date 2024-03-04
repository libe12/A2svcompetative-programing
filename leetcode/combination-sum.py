class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []
        cmp = []

        def backtrack(s):
            if sum(cmp) > target:
                return
            if sum(cmp) == target:
                ans.append(cmp[:])

            for i in range(s,len(candidates)):

                cmp.append(candidates[i])

                backtrack(i)

                cmp.pop()


        backtrack(0)

        return ans 


        