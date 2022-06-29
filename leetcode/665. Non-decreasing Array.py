class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        once = False
        max_prev = 1
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1] and not once:
                if max_prev > nums[i+1]:
                    nums[i+1]= nums[i]
                once = True
            elif nums[i]>nums[i+1] and once:
                return False
            max_prev = nums[i]
            
        return True