class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1:
            return 1
        a = k
        arr=[]
        ans = [0]*n
        for i in range(1,n+1):
            arr.append(i)
        freq = 0
        r = 0
        while True:
            if r == len(arr):
                r = 0
            if ans[r] == 1:
                r+=1
                continue
            a-=1
            if a == 0:
                
                ans[r]=1
                freq += 1
                a=k
            if freq == len(arr)-1:
                break
            r+=1
            
        for num in range(n):
            if ans[num]==0:
                return arr[num]
            

        