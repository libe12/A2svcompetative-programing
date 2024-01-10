class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        checked = set()
        res = 0
        for r in range(len(nums)):
            while nums[r] in checked:
                checked.remove(nums[l])
                l+=1

            checked.add(nums[r])
            res = max(res,sum(checked))
        return res

        

        