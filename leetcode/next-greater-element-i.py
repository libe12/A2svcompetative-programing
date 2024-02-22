class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        di = defaultdict(int)
        stk = []
        for i,num in enumerate(nums2):
            while stk and num >stk[-1]:
                di[stk.pop()] = num
                
            stk.append(num)

        n = len(nums1)
        ans = []

        for i in range(n):
            if nums1[i] in di.keys():
                ans.append(di[nums1[i]])
            else:
                ans.append(-1)
        return ans