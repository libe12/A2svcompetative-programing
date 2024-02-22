class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        stk_par={'(':')' , '{':'}' , '[':']'}
        print(stk_par.keys())
        for par in s:
            if par in stk_par.keys():
                stk.append(par)
            elif stk==[] or par!=stk_par[stk.pop()]:
                return False
        return stk==[]

'''
                stack=[]
        oc={'(' : ')', '{' : '}', '[' : ']', }
        for i in s:
            if i in oc.keys():
                stack.append(i)
            elif stack==[] or i!=oc[stack.pop()]:
                return False
        return stack==[]

'''