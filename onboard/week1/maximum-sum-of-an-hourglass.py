class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        def new_sum(i,j):
            res = sum (grid[i-1][j-1:j+2]) + grid[i][j] + sum (grid[i+1][j-1:j+2])
            return res
        
        row = len(grid)
        col = len(grid[0])
        updated_sum = 0
        max_sum = float('-inf')

        for i in range(1,row-1):
            for j in range(1,col-1):
                updated_sum = max(updated_sum, new_sum(i, j))
                max_sum = updated_sum
                
        return max_sum
        