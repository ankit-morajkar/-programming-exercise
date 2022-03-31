class Solution(object):
    def splitArray(self, nums, m):             
        def ispossible(x):
            splits = 0
            cumm_sum = 0
            for num in nums:
                cumm_sum = cumm_sum + num
                if cumm_sum > x:
                    cumm_sum = num
                    splits +=1
                    if splits >= m:
                        return False
                    
            return True
                    
        # Binary Search 
        max_element = 0
        num_sum = 0
        for num in nums:
            if num>max_element:
                max_element = num
                
            num_sum = num_sum + num
            
        while max_element<num_sum:
            mid = (max_element+num_sum)//2
            if ispossible(mid):
                num_sum = mid
            else:
                max_element = mid+1
                
        return max_element