class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        arr = len(strs[0])
        print(arr)
        res=strs[:arr]
        for num in strs:
            if len(num)<=arr:
                arr=len(num)
                res=num[:len(num)]
                
        
        for i in range(len(strs)):
            while arr >0 and strs[i][:arr]!=res[:arr]:

                arr-=1

           
        return res[:arr] if arr else ""
            

        