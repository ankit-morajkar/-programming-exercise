class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = True
        if (dividend>0) != (divisor>0):
            positive = False
            
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        if dividend<divisor:
            return 0
        
        ans = 0
        
        def find(left,divisor):
            current = divisor
            b = 1
            while current+current <=left:
                current += current
                b += b
            return left - current,b
        
        left = dividend
        
        while left >= divisor:
            left,b = find(left,divisor)
            ans += b
            
        if positive:
            return min(ans, (1<<31)-1)
        else:
            return max(-ans, -(1<<31))