class Solution:
    def minDeletions(self, s: str) -> int:
        counts = collections.Counter(s).values()
        
        s = set()
        total = 0
        for x in counts:
            while x in s and x>0:
                x -= 1
                total += 1
                
            s.add(x)
            
        return total