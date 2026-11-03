class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #[a,b] b->a
        graph=defaultdict(list)
        indegree=numCourses*[0]
        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u]+=1
        dq=deque(i for i in range(numCourses) if indegree[i]==0)
        result=[]
        while dq:
            node=dq.popleft()
            result.append(node)
            for neighbor in graph[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    dq.append(neighbor)
        if len(result)!=numCourses:
            return []
        return result
