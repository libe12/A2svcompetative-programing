# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
                # If either linked list is empty, return the other linked list
            if not l1:
                return l2
            if not l2:
                return l1

            # Create a dummy node to hold the head of the merged list
            dummy = ListNode(-1)
            # Create a pointer to the head of the merged list
            curr = dummy

            # Compare the values of the nodes pointed to by the two pointers
            # and take the smaller value to create a new node
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next

            # Append the remaining nodes of the non-empty linked list
            if l1:
                curr.next = l1
            if l2:
                curr.next = l2

            # Return the head of the merged list
            return dummy.next
        

        
        
        

            
        