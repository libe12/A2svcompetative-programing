class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diag = defaultdict(list)
        union = 0
        for i in range(len(mat)):
            for j in range(len(mat)):
             
                if i-j==0:
                    if i+j -(i-j) == len(mat)-1:
                        union = mat[i][j]
                    else:
                    
                        diag[i-j].append(mat[i][j])
                elif i+j ==len(mat)-1:
                    diag[i+j].append(mat[i][j])

        res = 0      
        for key,val in diag.items():
            res +=sum(val)
        return res + union
                