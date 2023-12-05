class Solution:
    def printVertically(self, s: str) -> List[str]:
        
        ans = []
        res = s.split()
        arr = max(len(iner_list)for iner_list in res)
        for i in range(arr):
            cur=''
            for word in res:
                if len(word)>i:
                    cur+=word[i]
                else:
                    cur+=' '
                
            ans.append(cur.rstrip())
            print(ans)
            
        return ans
            
      
                

                
                