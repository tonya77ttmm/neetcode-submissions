class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #b->a [a,b]
        graph=defaultdict(list)
        indegree=[0]*numCourses
        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u]+=1
        dq=deque(i for i in range(numCourses) if indegree[i]==0)
        result=0
        while dq:
            node=dq.popleft()
            result+=1
            for neighbor in graph[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    dq.append(neighbor)
        if result!=numCourses:
            return False
        return True