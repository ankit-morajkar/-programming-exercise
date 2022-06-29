class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        l = 0
        r = 1
        visited = set()
        visited.add(nums[l])
        global_max = nums[l]
        local_max = global_max
        while r<N:
            if nums[r] not in visited:
                visited.add(nums[r])
                local_max += nums[r]
                global_max = max(global_max, local_max)
                r += 1
                
            else:
                visited.remove(nums[l])
                local_max -= nums[l]
                l += 1
                
        return global_max