class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen=dict() #number: indice
        for i, num in enumerate(numbers):
            if (target-num) in seen:
                return [seen[target-num]+1, i+1]
            seen[num]=i
        