class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row,col = len(matrix), len(matrix[0])
        self.pre = [[0]*(col+1) for r in range(row +1)]
        for r in range(row):
            pref = 0
            for c in range(col):
                pref += matrix[r][c]
                above = self.pre[r][c+1]
                self.pre[r+1][c+1] = pref + above
        print(self.pre)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 +1, col1+1, row2+1,col2+1
        
        bottom_left = self.pre[row2][col1-1]
        top_right = self.pre[row1-1][col2]
        above = self.pre[row1-1][col1-1]
        bottom_right  = self.pre[row2][col2]

        return bottom_right + above - bottom_left - top_right
        

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)