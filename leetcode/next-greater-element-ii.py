

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:   
        
        diction={}
        stack=[]
        arr=[]
        res=[]
        
        
        for num in nums:
            arr.append(num)

        for num in nums:
            arr.append(num)
      
        for i in range(len(arr)):
            while i <len(arr) and stack and arr[i]>arr[stack[-1]]:
                diction[stack[-1]]=arr[i]
                
                stack.pop()
            

            stack.append(i)

        for i in range(len(stack)):
            diction[stack[i]]=-1

        for i in range(len(arr)):
            res.append(diction[i])


        
           
        print(res)
        return res[:len(nums)]

        