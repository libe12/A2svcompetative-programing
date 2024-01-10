class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        visited = set() 
        for i in range(n):
            if i not in visited:
                cycle = set()
                while True:

                    if i in cycle:
                        return True
                    visited.add(i)
                    cycle.add(i) 
                    prev, i = i, (i + nums[i])%n
                    
                    if prev == i:
                        break
                    #if i in visited:
                        #break
                    if nums[prev]>0 != nums[i]<0 :
                        break
        return False
                

       

        