class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk = []
        
        for i in range(len(s)):
            if not stk:
                stk.append(s[i])
            
            elif s[i]==stk[-1]:
                stk.append(s[i])
            else:
                if stk[-1]=='(' and s[i]==')':
                    stk.pop()
                else:
                    stk.append(s[i])
        return len(stk)
