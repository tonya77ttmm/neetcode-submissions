class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # open_=n
        # close=n
        path=[]
        res=[]
        
        def dfs(op, close):
            if op==n and close==n:
                res.append("".join(path))
                return
            for p in ["(",")"]:
                #append"(
                if p =="(" and op>=n:
                    continue
                #append")
                if p==")" and close>=op:
                    continue
                path.append(p)
              
                dfs(op+(1 if p=="(" else 0),close+(1 if p==")" else 0))

                path.pop()
        dfs(0,0)
        return res