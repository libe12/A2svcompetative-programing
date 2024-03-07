class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        left,right = 0, len(matrix)-1

        while left <= right:
            rmid = (left + right)//2

            start, end = 0, len(matrix[0])-1

            while start <= end:
                cmid = (start + end)//2

                if matrix[rmid][cmid] == target:
                    return True

                elif matrix[rmid][cmid] > target:
                    right = rmid -1

                    end = cmid -1
                else:
                    left = rmid + 1
                    start = cmid + 1
        return False


        