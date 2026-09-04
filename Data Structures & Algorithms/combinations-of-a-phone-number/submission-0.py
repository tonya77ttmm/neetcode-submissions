class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #dict={2:"abc",3:"def"}
        if not digits:
            return []
        d={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        result=[]
        def dfs(path,index):
            if len(path)==len(digits):
                result.append("".join(path))
                return
            options=d[int(digits[index])]
            for c in options:
                path.append(c)
                dfs(path,index+1)
                path.pop()

        dfs([],0)
        return result
