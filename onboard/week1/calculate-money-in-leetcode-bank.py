class Solution:
    def totalMoney(self, n: int) -> int:
        start = 1
        res = 0
    
        for i in range(1, n+1):
            if i % 7 == 1:
                start =  ((i // 7) + 1)
                
            res += start 
            start += 1
            
           
        return res
     