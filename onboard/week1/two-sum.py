class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_di = defaultdict(int)

        for i, num in enumerate(nums):
            sum_tar = target - num

            if sum_tar in my_di:
                return [my_di[sum_tar], i]
                
            my_di[num] = i
        
        
        