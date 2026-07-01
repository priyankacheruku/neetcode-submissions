class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d_map = {}
        for i in nums:
            if d_map.get(i):
                return True
            else:
                d_map[i] =1
        return False
        