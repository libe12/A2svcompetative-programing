class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        i=0
        for num in zip(*matrix):
            num = reversed(num)
            num = list(num)
            matrix[i] = num
            i+=1
    

       