# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
   
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
            
            slow = fast = head
            
            if head == None:
                return head
            
            while fast:
                while fast and slow.val == fast.val:
                    fast = fast.next
                slow.next = fast
                slow = fast
                
            return head