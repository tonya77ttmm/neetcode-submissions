# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the middle point
        slow, fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next     
        #reverse the second half
        second=slow.next
        slow.next=None

        prev=None
        cur=second
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        second=prev
        #merge two lists
        first=head
        while second:
            n1=first.next
            n2=second.next
            first.next=second
            second.next=n1
            first=n1
            second=n2
        






        