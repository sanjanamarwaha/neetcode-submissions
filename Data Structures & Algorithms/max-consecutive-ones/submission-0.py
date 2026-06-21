class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for j in range(len(nums)):
            if nums[j] == 1:
                count += 1
            else:
                if count > res:
                    res = count
                count = 0
        if count > res:
            res = count
        return res
