class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 0
       
        for i in range(n):
            r = max(grid[i])
            l = 0
            for j in zip(*grid):
                c = max(j)

                res = min(c,r)

                ans += res - grid[i][l]

                l += 1
                if l == len(j):
                    break
            

        return ans
