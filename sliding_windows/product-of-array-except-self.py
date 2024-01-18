class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        res = 1
        for num in nums:
            if num!=0:
                res *= num
        ans = []
        for i, num in enumerate(nums):
            if num ==0 and c[num] == 1:
                ans .append(res)
            elif num ==0 and c[num] > 1:
                ans.append(0)
            elif num !=0 and 0 not in c:
                ans.append(res//num)
            elif num !=0 and 0 in c:
                ans.append(0)
        return ans

