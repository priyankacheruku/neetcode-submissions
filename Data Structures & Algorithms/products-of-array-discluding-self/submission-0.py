class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l= len(nums)
        res = [1]*l
        for i in  range(l):
            for j in range(l):
                if i!=j:
                    res[j] = res[j]*nums[i]
        # print(res)
        return res

        