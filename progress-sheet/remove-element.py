class Solution:
    def removeElement(self, s: List[int], val: int) -> int:
        l = r = 0 
        for r in range(len(s)):
            if s[l] ==val and s[r]!=val:
                s[l],s[r] = s[r], s[l]
                l+=1
                continue
            elif s[l]!=val and s[r] != val:
                
                l+=1
        return l
            


        