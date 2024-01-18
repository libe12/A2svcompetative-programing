class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        final_pos = 0
        for pas, start, end in trips:

            final_pos = max(final_pos,end)
            
        ans = [0]*(final_pos+1)
        for pas,start,end in trips:
            ans[start] += pas
            ans[end] -= pas
        for i in range(1,len(ans)):
            ans[i] += ans[i-1]
        
        if max(ans)>capacity:
            return False
        return True
