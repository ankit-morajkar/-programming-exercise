class Solution:
    def countVowelStrings(self, n: int) -> int:
        def count(index, last):
            if index == n:
                return 1
            
            total = 0
            for i in range(last,5):
                total +=count(index+1,i)
                
            return total
        
        total = 0
        for i in range(0,5):
            total +=count(1,i)
            
        return total