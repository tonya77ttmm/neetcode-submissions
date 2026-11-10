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
                return 
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
            
        count=0
        #iterate through graph
        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1
        return count
