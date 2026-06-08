class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closeToOpen={")":"(","}":"{","]":"["}
        #closing brackets as keys since it triggers a check
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1]==closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack)==0