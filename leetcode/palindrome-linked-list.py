# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Initialize three pointers: prev, ptr and fast
        prev = None
        ptr = fast = head

        # Reverse the first half of the linked list
        while fast != None:
            # Move fast two steps at a time
            fast = fast.next
            if fast == None:
                
                ptr = ptr.next
                break
            fast = fast.next

          
            temp = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = temp

        while ptr != None:
            if ptr.val != prev.val:
               
                return False
            
            ptr = ptr.next
            prev = prev.next
        
       
        return True