class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod , count = 1, 0

        for i in range(n):
            if(nums[i] == 0):
                count+= 1
            else:
                prod*=nums[i]

        if count > 1:
            return [0] * n

        res = [0] * n
        for i, c in enumerate(nums):
            if count: res[i] = 0 if c else prod
            else: 
                res[i] = prod // c
        return res


