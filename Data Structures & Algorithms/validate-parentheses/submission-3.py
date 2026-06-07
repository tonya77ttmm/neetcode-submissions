class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping={")":"(","]":"[","}":"{"}
        for r in range(len(s)):
            #if s[r] is one of the close brackets
            if s[r] in mapping:
                #if stack is not empty and it can match its open bracket in the stack
                if stack and stack[-1]==mapping[s[r]]:
                    stack.pop()
                #there's no way that a close bracket is appended in the stack and can be poped afterwards
                else:
                    return False
            else:
                stack.append(s[r])
        return not stack