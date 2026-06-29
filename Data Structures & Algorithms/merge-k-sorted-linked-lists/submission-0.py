# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k=len(lists)
        if k<=0:
            return None
        for i in range(1,k,1):
            lists[i]=self.mergeTwoLists(lists[i-1],lists[i])
        return lists[k-1]
    
    def mergeTwoLists(self,list1,list2):
        dummy=ListNode(0)
        cur=dummy
        while list1 and list2:
            if list1.val<=list2.val:
                cur.next=list1
                list1=list1.next
            else:
                cur.next=list2
                list2=list2.next
            cur=cur.next
        cur.next=list1 or list2
        return dummy.next
