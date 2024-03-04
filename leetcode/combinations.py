class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        ans = []

        sub = []

        def backtrack(i,sub):

            if len(sub) == k:

                ans.append(sub.copy())
                return 
            if i > n:
                return 
            for j in range(i,n+1):

                sub.append(j)

                backtrack(j+1,sub)

                sub.pop()

        backtrack(1,[])

        return ans

        





        