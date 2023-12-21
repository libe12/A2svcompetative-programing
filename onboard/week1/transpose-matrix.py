class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        arr =[] 
        n = len(matrix)
        m = len(matrix[0])
        for i in range(m):
            res  = []
            for j in range(n):
                
                res.append(matrix[j][i])
            arr.append(res)
        return arr

'''
0   00   01   02

1   10    11   12

    0     1    2
    for i in range(len(matrix = 2))
        for j in range(len(matrix[0] = 3))
            arr.append (matrix[j][i])

            00, 10, 20
            01 ,11, 21
'''