class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = stop = 0
        for num in nums:
            if num == 1:
                stop += 1
            else:
                if res < stop:
                    res = stop
                stop = 0

        return res if res > stop else stop
