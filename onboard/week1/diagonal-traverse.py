class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col = len(mat[0])

        dictl = defaultdict(list)

        for i in range(row):
            for j in range(col):
                dictl[i+j].append(mat[i][j])

        arr = []
        for key, val in dictl.items():
            if key % 2 == 0:
                arr += reversed(val)
            else:
                arr += val
        return arr

                
                
