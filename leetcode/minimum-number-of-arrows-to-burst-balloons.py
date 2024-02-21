class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        print(points)
        l = 0
        i = 1
        n = len(points)
        ans = 1
        while i < n:
            if points[l][1] <= points[i][1] and points[l][1]>=points[i][0]:
                i += 1
                
            else:
                ans += 1
                l = i
                i += 1
                   
        return ans
        