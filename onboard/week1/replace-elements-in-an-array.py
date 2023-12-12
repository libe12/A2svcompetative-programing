class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        my_di = defaultdict(int)
        for i, val in enumerate(nums):
            my_di[val] = i
       
        for num, replace in operations:
            nums[my_di[num]] = replace

            cur_idx = my_di[num]
            del my_di[num]
            my_di[replace] = cur_idx
           

        return nums



            

        