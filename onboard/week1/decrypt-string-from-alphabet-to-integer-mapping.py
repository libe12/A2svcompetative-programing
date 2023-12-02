class Solution:
    def freqAlphabets(self, s: str) -> str:
        l = 0
        r = 2
        res=''
        while l<len(s) and r<len(s):
            if s[r]=='#':
                res+=chr(96+int(s[l:r]))
                l=r+1
                r=r+3
            else:
                res+=chr(96+int(s[l]))
                l+=1
                r+=1
        print(l)
        while l<len(s):
            res+=chr(96+int(s[l]))
            l+=1
        
        return res
        