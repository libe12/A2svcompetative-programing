class Solution: 
    def select(self, arr, i):
        return
            
    def selectionSort(self, arr,n):
        for i in range(len(arr)):
            min_index=i
            for j in range(i+1,len(arr)):
                if arr[j]<arr[min_index]:
                    min_index=j
            if min_index!=i:
                arr[i],arr[min_index]=arr[min_index],arr[i]
                    
