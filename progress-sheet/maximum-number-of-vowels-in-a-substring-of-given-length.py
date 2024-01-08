class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        l = r = 0
        ans = res = 0
        st = 'aeiou'
        while r < len(s):
            if r-l+1 <=k:
                if s[r] in st:
                    ans += 1
                r+=1
                
            else:
                if s[l] in st:
                    ans-=1
                l+=1
                
            res = max(res,ans)
                
        return min(res,k)
        