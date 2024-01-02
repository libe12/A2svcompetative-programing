class Solution:
    def smallestNumber(self, num: int) -> int:
        # sort the num by changing int to the string form 
        string = sorted(str(abs(num)),reverse=num<0) # if num is greater than zero sort in ascending order else you just have to sort in reversed order 


        # get the first none zero element with the next argument 
        not_zero = next((i for i,n in enumerate(string) if n!='0'),0 )

        # swap the first non zero element with zero
        string[0],string[not_zero] = string[not_zero], string[0]

        return int(''.join(string)) if num>0 else -1*int(''.join(string))