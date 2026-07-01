class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for i in nums:
            counter[i] = 1+counter.get(i,0)
        return sorted(counter,key=counter.get,reverse=True)[:k] 