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
        cur=head
        d={None:None} #create a hashmap to map the original node to its copy node
        while cur:
            copy=Node(cur.val)
            d[cur]=copy
            cur=cur.next
            
        cur=head
        while cur:
            copy=d[cur]
            copy.next=d[cur.next]
            copy.random=d[cur.random]
            cur=cur.next

        return d[head]

