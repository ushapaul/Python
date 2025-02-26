class Solution:
    def largestOddNumber(self, num: str) -> str:
        ans=""
        for i in range(len(num)):
            if (int(num[i])%2==1):
                ans=num[0:i+1]
        return ans
