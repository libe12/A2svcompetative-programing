class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
       
        arr = [0]*(n+1)
        
        for i in range(len(bookings)):
            arr[bookings[i][0]-1] += bookings[i][2]
            arr[bookings[i][1]] -= bookings[i][2]
           
        for i in range(1,len(arr)):
            arr[i] += arr[i-1]
        arr.pop()
        return arr