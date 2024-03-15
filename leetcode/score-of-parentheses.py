class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans,val = 0, 0
        stack = []
        for p in s:
            if p=='(':
                stack.append(0)
            else:
                mul = stack.pop()

                if mul > 0:
                    val = 2*mul
                else:
                    val = 1
                if not stack:
                    ans += val
                else:
                    stack[-1] += val
            
        return ans
        