class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])

            else:
                cur_str = ''
                while stack[-1] != '[' :
                    cur_str = stack.pop() + cur_str
                stack.pop()
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k 


                stack.append(int(k)*cur_str)
        return ''.join(stack)
                
        