class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        num_edges=len(edges)
        if num_edges!=n-1:
            return False
        graph=[[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visit=set()
        def has_cycle(node,parent):
            if node in visit:
                return True
            visit.add(node)
            for neighbor in graph[node]:
                if neighbor==parent:
                    continue
                if has_cycle(neighbor,node):
                    return True
                
            return False
        return not has_cycle(0,-1) and len(visit)==n

        