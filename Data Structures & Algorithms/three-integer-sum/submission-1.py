class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        ans = []
        nums.sort()
        for i in range(N-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            temp_target = 0 -nums[i]
            d = {}
            l,r = i+1,N-1
            while l<r:
                curr = nums[l]+nums[r]
                if temp_target ==curr:
                    ans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1

                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                elif curr<temp_target:
                    l +=1
                else:
                    r-=1
                
            # for j in range(i+1,N):
            #     if nums[j] in d:
            #         ans.append([nums[i],d[nums[j]],nums[j]])
            #     else:
            #         curr = temp_target-nums[j] 
            #         d[curr] = nums[j]

        return ans
        