class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        dic={}
        counter=0

        
        for i in nums:
            if i in dic:
                counter=counter+dic[i]
                dic[i]=dic[i]+1
            else:
                dic[i]=1
        return counter
