class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        res = ''
        for num in digits:
            res+=str(num)
        
        appd = str(int(res) + 1)
        
        arr =[]
        for num in appd:
            arr.append(int(num))
        return arr