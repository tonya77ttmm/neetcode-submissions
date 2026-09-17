"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        #bfs
        dq=deque([node])
        oldToNew={} #oldNode: newClonedNode
        oldToNew[node]=Node(node.val)
        while dq:
            n=dq.popleft()
            for neighbor in n.neighbors:
                if neighbor not in oldToNew:
                    dq.append(neighbor)
                    oldToNew[neighbor]=Node(neighbor.val)
                oldToNew[n].neighbors.append(oldToNew[neighbor])
        return oldToNew[node]