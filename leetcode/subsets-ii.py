class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        checked = set()
        ans = []
        path = []
        def backtracking(s):

            if tuple(path[:]) not in checked:
                ans.append(path[:])
            checked.add(tuple(path[:]))

            for i in range(s,len(nums)):
                path.append(nums[i])

                backtracking(i+1)

                path.pop()

        backtracking(0)

        return ans
        