class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        r=0
        if n ==1:
            return True
        while r < n:
            arr = 3**r
            if arr > n:
                arr = 3**(r-1)
                while arr < n:
                    r-=1
                    arr+=3**(r-1)
                    if arr >n:
                        arr-=3**(r-1)
                    else:
                        if r<=0:
                            return False
                    
                if arr == n:
                    return True
            r+=1
        return False
        
        