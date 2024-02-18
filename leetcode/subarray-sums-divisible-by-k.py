class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        visited= defaultdict(int)
        visited[0] = 1
        res = 0
        cur_sum = 0
        for num in nums:
            cur_sum += num
            rem = cur_sum%k
            
            res += visited[rem]
            visited[rem] += 1
        return res


        