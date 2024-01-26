# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        priv=None
        cur=head
        while cur:
            temp=cur.next
            cur.next=priv
            priv=cur
            cur=temp
            
        return priv

    """
    
    n<-1<-2<-3  head=3
          |  |
    cur.next=n
       


    """