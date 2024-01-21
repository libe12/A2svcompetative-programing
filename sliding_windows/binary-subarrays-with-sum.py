class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        visited = defaultdict(int)
        visited[0] = 1
        count = 0
        for i in range(1,len(nums)):
            nums[i] += nums[i-1] 
        for i in range(len(nums)):
            if nums[i] - goal in visited:
                count += visited[nums[i]-goal]
            visited[nums[i]] += 1
        return count