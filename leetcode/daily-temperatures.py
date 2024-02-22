class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for val,key in enumerate(temperatures):
            while stack and key>stack[-1][0]:
                stackT,stackI=stack.pop()
                res[stackI]=(val-stackI)
            stack.append([key,val])
        return res

            