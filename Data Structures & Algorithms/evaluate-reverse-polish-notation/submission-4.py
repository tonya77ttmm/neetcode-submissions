class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators={"+","-","*","/"}#数组查找o1？
        for token in tokens:
            if token in operators:
                op1=stack.pop()
                op2=stack.pop()
                if token == "+":
                    res=op1+op2
                elif token=="-":
                    res=op2-op1
                elif token == "*":
                    res=op1*op2
                elif token == "/":
                    res=int(op2/op1)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack.pop()
            
        