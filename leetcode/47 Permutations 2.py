class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        count = {n:0 for n in nums}
        for n in nums:
            count[n] +=1
            
        def recur():
            #base case
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
                
            else:
                for ele in count:
                    if count[ele]>0:
                        perm.append(ele)
                        count[ele] -=1
                        recur()
                        count[ele] +=1
                        perm.pop()
                    
        recur()
        return res