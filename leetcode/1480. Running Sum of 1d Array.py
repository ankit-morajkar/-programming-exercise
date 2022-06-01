class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        N = len(nums)
        dp = [nums[0]]
        if len(nums)==1:
            return dp
        dp.append((nums[0]+nums[1]))
        for i in range(2,N):
            next = dp[i-1]+nums[i]
            dp.append(next)
            
        return dp