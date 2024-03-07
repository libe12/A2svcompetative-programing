class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def check(capacity):

            time = 0

            for i in range(len(piles)):

                time += ceil(piles[i]/capacity)

            return time
            

        left = 1
        right = max(piles)
        
        while left <= right:

            mid = (left + right)//2

            if check(mid) > h:
                left = mid + 1
                
            else:
                right = mid - 1
            
            
        return left
                






        