class Solution:
    def subarraySum(self, arr: List[int], k: int) -> int:
        dict_sum={0:1}
        count=0
        s=0
        for num in arr:
            s+=num
            if s-k in dict_sum:
                count+=dict_sum[s-k]
            if s in dict_sum:
                dict_sum[s]+=1
            else:
                dict_sum[s]=1
        return count
        
            
        