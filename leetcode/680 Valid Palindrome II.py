class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s)-1
        count = 0
        
        def ispalindrome(x):
            print(x)
            lf = 0
            rf = len(x)-1
            while lf<rf:
                if x[lf] == x[rf]:
                    lf +=1
                    rf -=1
                else:
                    return False
            
            return True
        
        while l<r:
            if s[l] == s[r]:
                l +=1
                r -=1
            elif count == 0:
                count += 1
                if ispalindrome(s[l:r]) or ispalindrome(s[l+1:r+1]):
                    return True
                    
            else:
                return False
        return True