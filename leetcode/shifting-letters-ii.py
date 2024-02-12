class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        strs = [0]*(len(s)+1)
        ans = []
        for start,end,dirc in shifts:
            if dirc == 0:
                strs[start] -=1
                strs[end+1] +=1
            else:
                strs[start] +=1
                strs[end+1] -=1
        for i in range(1,len(strs)):
            strs[i] += strs[i-1]
        for i,num in enumerate(s):
            res = ((ord(s[i])-97)+(strs[i]))%26
            ans.append(chr(res+97))
        
        return ''.join(ans)
        