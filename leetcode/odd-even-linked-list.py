# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        oddp = cur =  head
        evenp = evenhead = head.next
        i = 1
        while cur:
            if i>2 and i%2!=0:
                oddp.next = cur
                oddp = oddp.next
            if i>2 and i%2==0:
                evenp.next = cur
                evenp = evenp.next
            cur = cur.next
            i+=1
        evenp.next = None
        oddp.next = evenhead
        return head

        
        