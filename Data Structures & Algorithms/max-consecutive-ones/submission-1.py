class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        r = 0
        c = 0
        for i in nums:
            if i==1:
                c+=1
            elif i==0:
                c=0
            r = max(c,r)
        return r
        