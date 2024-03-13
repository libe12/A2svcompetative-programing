class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        n = len(tokens)
       
        for i in range(n):
            if tokens[i]=='*' and len(stack) > 1:
                res = stack.pop()*stack.pop()
                stack.append(res)
                continue
            if tokens[i] == '/' and len(stack)>1:
                res1 = stack.pop()
                res2 = stack.pop()

                res = res2 / res1

                if res > 0:
                    stack.append(floor(res))
                else:
                    stack.append(ceil(res))
                continue
            if tokens[i]=='+' and len(stack) > 1:
                res = stack.pop() + stack.pop()
                stack.append(res)
                continue
            if tokens[i] =='-' and len(stack) > 1:
                res1 = stack.pop()
                res2 = stack.pop() 
                stack.append(res2-res1)
                continue
            stack.append(int(tokens[i]))
       
        return stack[0]
        

                


        