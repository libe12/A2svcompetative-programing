class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pref = [0]
        r = len(nums) -1
        for i in range(len(nums)):
            pref.append(nums[i]+pref[-1])
        res = [0]*len(nums)
        for i in range(len(nums)):
            res[i] =pref[-1] -pref[i+1]-(nums[i]*(r-i)) + nums[i]*(i+1)-pref[i+1]
        return res
            


        