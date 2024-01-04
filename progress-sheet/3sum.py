class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        result=[]
        for i in range(n-2):
            if i >0 and nums[i]==nums[i-1]:
                continue
            l, r= i+1, n-1
            
            while l<r :
                total=nums[l]+nums[r]+nums[i]
                if total<0:
                    l+=1
                elif total>0:
                    r-=1
                else:
                    result.append([nums[l],nums[r],nums[i]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1    
                    l+=1
                    r-=1
        return result
                