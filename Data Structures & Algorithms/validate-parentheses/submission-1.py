class Solution:
    def isValid(self, s: str) -> bool:
        #stack
        #if stack:
        #    
        #   if s[r]==')' and stack[-1]=='(':
        #       stack.pop()
        #   elif s[r]=='}' and stack[-1]=='{':
        #       stack.pop()
        #   elif s[r]==']' and stack[-1]=='[':
        #       stack.pop()
        #else
        # stack.append(s[r])
        q=collections.deque()
        for r in range(len(s)):
            if q and ((s[r]==')' and q[-1]=='(' )or (s[r]=='}' and q[-1]=='{') or (s[r]==']' and q[-1]=='[')):
                q.pop()
            else:
                q.append(s[r])
        return not q