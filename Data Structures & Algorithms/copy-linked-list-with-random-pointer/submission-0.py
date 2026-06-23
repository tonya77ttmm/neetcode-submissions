"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy=Node(0)
        copy=dummy

        cur=head

        d={}
        while cur:
            cur_copy=Node(cur.val)
            copy.next=cur_copy
            d[cur]=cur_copy
            cur=cur.next
            copy=copy.next
            
        
        cur=head
        copy=dummy.next
        while cur:
            copy.random=d[cur.random] if cur.random else None
            cur=cur.next
            copy=copy.next
        return dummy.next

