# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        sum_n=dummy
        carry=0
        while l1 and l2:
            cur_val=(l1.val+l2.val+carry)%10
            carry=(l1.val+l2.val+carry)//10
            sum_n.next=ListNode(cur_val)
            l1=l1.next
            l2=l2.next
            sum_n=sum_n.next
            
        l=l1 or l2
        while l:
            cur_val=(l.val+carry)%10
            carry=(l.val+carry)//10
            sum_n.next=ListNode(cur_val)
            l=l.next
            sum_n=sum_n.next
        if carry!=0:
            sum_n.next=ListNode(carry)
        return dummy.next



