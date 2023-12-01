class Solution:
    def romanToInt(self, s: str) -> int:
        std = {'I':1 ,'V':5, 'X':10, 'C':100, 'L':50, 'D':500, 'M':1000}
        res = []
        for i, num in enumerate(s):
            if not res:
                res.append(std[num])
            elif std[num]>res[-1]:
                res.append(std[num]-2*(res[-1]))
            else:
                res.append(std[num])
        return sum(res)