class Solution:
    def moveZeroes(self, nums):
        d=[]
        c=0
        for i in range (len(nums)):
            if(nums[i]!=0):
                d.append(nums[i])
            else:
                c+=1
        for i in range (c):
            d.append(0)
            nums[:]=d
