class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited=set()
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        #build the graph
        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
            return 1
        count=0
        #iterate through graph
        for i in range(n):
            count+=dfs(i)
        return count
