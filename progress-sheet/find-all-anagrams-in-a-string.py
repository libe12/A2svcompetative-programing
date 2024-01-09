class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res =[]
        st = sorted(p)
        
        for i in range(len(p)-1,len(s)):
            if st==sorted(s[i-len(p)+1:i+1]):
                res.append(i+1-len(p))
        return res

        