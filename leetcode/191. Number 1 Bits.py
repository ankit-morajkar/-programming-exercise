class Solution:
    def hammingWeight(self, n: int) -> int:
        s = bin(n)
        ans = 0
        for x in s:
            if x == '1':
                ans +=1
                
        return ans