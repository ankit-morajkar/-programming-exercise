class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        def binary_search(nums, target, i):
            n = len(nums)
            
            if n == 1 and nums[0]!=target:
                return -1
            
            if n == 0:
                return -1
            
            if n == 1 and nums[0]==target:
                return i

            if n%2 == 1:
                if nums[(n-1)/2]==target:
                    return i+(n-1)/2
                elif nums[(n-1)/2]>target:
                    return binary_search(nums[0:(n-1)/2],target,i)
                elif nums[(n-1)/2]<target:
                    return binary_search(nums[(n+1)/2:],target, i+(n+1)/2)

            else:
                if nums[n/2]==target:
                    return i+(n/2)
                elif nums[n/2]>target:
                    return binary_search(nums[0:n/2],target,i)
                elif nums[n/2]<target:
                    return binary_search(nums[(n/2)+1:],target, i+(n/2)+1)
            
        return binary_search(nums, target, 0)