from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d=Counter(nums)
        n=len(nums)
        for ele in d:
            if (d[ele]>n//2):
                return ele
        return -1
