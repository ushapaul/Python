class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        
        idx = 0

        for i in range(3):
            freqency = count.get(i, 0)
            nums[idx : idx + freqency] = [i] * freqency
            idx += freqency
