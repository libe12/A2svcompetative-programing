class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        mind =  float('inf')
        ans = 0
        nums.sort()
        if len(nums)==3:
            return sum(nums)

        for i in range(len(nums)-2):
            val = nums[i]
            l = i+1
            r = len(nums)-1 

            while r > l:
                
                res = val+nums[l]+nums[r]
                
                if abs(target-res) < mind  :
                    mind = abs(target-res)
                    ans = res
                    
                if res < target:
                    l+=1
                if res > target:
                    r-=1
                if res==target:
                    return res
        

        return ans