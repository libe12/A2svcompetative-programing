class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res1 = []
        res2 = []
        res = []
        for num in nums:
            if num <0:
                res1.append(num)
            else:
                res2.append(num)
        for i in range(len(nums)//2+1):
            if len(res2) > i:
                res.append(res2[i])
            if len(res1) >i:
                res.append(res1[i])
        return res
