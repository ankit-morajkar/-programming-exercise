class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        for i in range(N):
            if i != nums[i]:
                return i
        return N