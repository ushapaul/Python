class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        maxi=0
        nums.sort()
        for i in range(len(nums)):
            if maxi!=nums[i]:
                maxi=(nums[i])
            else:
                return maxi
