class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        max_can = max(candies)
        print(max_can)
        for i in range(len(candies)):
            sum_cand = candies[i] + extraCandies
            
            if sum_cand >=max_can:
                candies[i]=True
            else:
                candies[i]=False
            
            
        return candies