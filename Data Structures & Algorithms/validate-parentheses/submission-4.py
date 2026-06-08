class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                #]]] no corresponding bracket
                if not stack:
                    return False
                if c == ")":
                    if stack.pop()!="(":
                        return False
                elif c=="]":
                    if stack.pop()!="[":
                        return False
                elif c=="}":
                    if stack.pop()!="{":
                        return False
        return len(stack)==0
