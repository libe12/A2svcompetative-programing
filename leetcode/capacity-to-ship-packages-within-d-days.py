class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        
        def checker(capacity):
            count = 0
            sum_ = 0
        
            for i in range(len(weights)):
                
                if sum_+ weights[i] > capacity:
                    count += 1
                    sum_=0
                sum_+= weights[i]
            
            return count >= days
                

        left = max(weights)
        right = sum(weights)

        while left <= right:
           
            mid = (left + right)//2

            if checker(mid):
                left = mid + 1
            else:
                right = mid - 1

        return left