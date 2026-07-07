class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)-1
        for i in range(n):
            l,r = i+1,n
            temp_target = target - numbers[i]
            while l<=r:
                mid = l+(r-l)//2
                curr = numbers[mid]
                if curr==temp_target:
                    return [i+1,mid+1]
                elif curr>temp_target:
                    r = mid-1
                else:
                    l = mid+1
        return []


        
        