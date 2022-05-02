class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans = []
        for ele in nums:
            if ele % 2 == 0:
                ans.append(ele)
        for ele in nums:
            if ele % 2 != 0:
                ans.append(ele)
        return ans