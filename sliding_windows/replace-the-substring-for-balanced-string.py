class Solution:
    def balancedString(self, s: str) -> int:

        d = {'W':0,'Q':0,'R':0,'E':0}
        n  = len(s)/4
        for i in range(len(s)):
            d[s[i]] += 1
        l = 0
        ans = len(s)
        for r in range(len(s)):
            d[s[r]] -= 1
            while d['W']<=n and  d['E']<=n and d['Q']<=n and d['R']<=n and l<len(s):
                ans  = min(ans,r-l+1)

                d[s[l]] +=1
                l += 1
        return ans
