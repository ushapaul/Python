class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res=[]
        strset=set(nums)
        n=len(nums)
        def backtrack(i):
            if i>n:
                return 
            if i not in strset:
                res.append(i)
                return res
            backtrack(i+1)
        backtrack(0)
        return res[0]
