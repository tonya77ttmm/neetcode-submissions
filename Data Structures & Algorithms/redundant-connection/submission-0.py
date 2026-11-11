class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent=list(range(n+1))
        size=[1]*(n+1)
        def find(a):
            if parent[a]!=a:
                parent[a]=find(parent[a])
            return parent[a]

        def union(a,b):
            rootA=find(a)
            rootB=find(b)
            if rootA==rootB:
                return False
            if size[rootA]<size[rootB]:
                rootA,rootB=rootB,rootA
            parent[rootB]=rootA
            size[rootA]+=size[rootB]
            return True
        for a,b in edges:
            if not union(a,b):
                return [a,b]
            