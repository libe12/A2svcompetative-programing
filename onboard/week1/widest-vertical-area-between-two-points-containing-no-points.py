class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        wide_len=0
        for i in range(1,len(points)):
            wide_len  = max(wide_len, points[i][0] - points[i-1][0])
        return wide_len



        