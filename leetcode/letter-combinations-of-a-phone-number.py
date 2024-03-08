class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        track = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'} 

        ans = []
        
        def backtrack(n,path):
            if n == len(digits):
                ans.append(''.join(path.copy()))
                return
            
            for val in track[digits[n]]:
                path.append(val)
                
                backtrack(n+1,path)

                path.pop()

        
        backtrack(0,[])
        if ans ==[""]:
            return []
        return ans
        

        
        