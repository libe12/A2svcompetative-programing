class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        queue = deque()
        ans = []
        for i in range(k):
            
            while queue and nums[i] > queue[-1][0]:
                queue.pop()
            queue.append([nums[i],i])
        ans.append(queue[0][0])
        for i in range(k,len(nums)):
            if (i-k) == queue[0][1]:

                queue.popleft()
            while queue and queue[-1][0] < nums[i]:
                queue.pop()
                
            queue.append([nums[i],i])
            
            ans.append(queue[0][0])
        return ans

        


        