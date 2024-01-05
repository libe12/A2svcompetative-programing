"""
name ="fikre"   typed="fffikkreeeex"      preve_char="r"
            |                  |
return = True
# check the edge cases for this example   n-length of name and m-length character of typed
   1-if we get all the element of the name before we checked the whole characters of the typed string
   2-what if the len(name ) is greatet than the len(typed) -we will return false
"""


from collections import *
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        left = right = 0
        while right < len(typed):
            if left < len(name) and name[left]==typed[right]:
                left+=1
                right+=1
            elif right > 0 and typed[right]==typed[right-1]:
                right+=1
            else:
                return False
        return left==len(name)

           
       
        
        
        


        







 
        