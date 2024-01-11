class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        count = 0
        ans  = 0
        l = 0
        odd = 0
        for r in range(len(nums)):

            if nums[r]%2!=0:
                count += 1
                odd = 0
            
            while count == k:
                odd += 1
                #print(odd)
                
                if nums[l]%2!=0:
                    count -= 1
                l +=1
            ans += odd
                
                
            
        return ans

