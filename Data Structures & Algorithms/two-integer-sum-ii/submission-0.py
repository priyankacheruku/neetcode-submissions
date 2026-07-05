class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        n = len(numbers)
        for i in range(n):
            req = target-numbers[i]
            if d.get(req,None) is not None:
                return [d[req],i+1]
            d[numbers[i]] = i+1

        
        