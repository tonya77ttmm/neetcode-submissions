# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #fast move k steps
        dummy=ListNode(0)
        dummy.next=head
        newtail=dummy #newtail after reverse this ksize list
        slow,fast=head,head
        prev=None #the head of the already reversed ksize list
        enoughk=True
        while fast:
            
            for i in range(k):
                if not fast:
                    enoughk=False
                    break
                fast=fast.next
            
            tmp=slow#record next new tail
            if not enoughk:
                newtail.next=slow
                break
            while slow!=fast and enoughk:
                nxt=slow.next
                slow.next=prev
                prev=slow
                slow=nxt
            
            newtail.next=prev
            newtail=tmp
            prev=None
            
        
        return dummy.next
