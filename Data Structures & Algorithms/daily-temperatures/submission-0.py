class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #next greater element
        #mono decreasing stack
        stack=[] #store the indices of temperature that hasn't found the next warmer day
        answers=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev=stack.pop()
                answers[prev]=i-prev
            stack.append(i)
        return answers