class Solution:
    def maxScore(self, s: str) -> int:
        res = []
        
        for i in range(len(s)):
            if res:
                res.append(int(s[i])+res[-1])
            else:
                res.append(int(s[i]))
        print(res)

        ans = 0   
        for i in range(len(res)-1):
            cur = (i+1)-res[i] + res[-1]-res[i]
            ans = max(ans,cur)
        return ans


        