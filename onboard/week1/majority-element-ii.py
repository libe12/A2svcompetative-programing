class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        apear_num =Counter(nums)
        arr = []
        res = len(nums)/3
        for num in apear_num:
            print(apear_num.values())
            if apear_num[num] > res:
                arr.append(num)
            #if num.values()
        return arr