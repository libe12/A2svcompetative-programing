class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort()

        ans = l = 0
        i = len(tasks)-1
        while i >=3:
            ans = max(ans, processorTime[l] + tasks[i])

            i -= 4
            l += 1

        return ans
        