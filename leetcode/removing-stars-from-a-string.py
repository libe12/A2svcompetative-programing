class Solution:
    def removeStars(self, s: str) -> str:
        stk = []
        for i in range(len(s)):
            if stk!=[] and s[i]=='*':
                stk.pop()
            elif s[i]!='*':
                stk.append(s[i])
        return ''.join(stk)

        