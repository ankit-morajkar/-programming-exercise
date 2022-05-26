class Solution:
    def maxPower(self, s: str) -> int:
        prev = ''
        mx = 1
        tmp = 1
        for c in s:
            if prev == c:
                tmp +=1
                mx = max(mx,tmp)
            else:
                tmp = 1
            prev = c
        return mx