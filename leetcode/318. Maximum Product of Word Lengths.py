class Solution:
    def maxProduct(self, words: List[str]) -> int:
        N = len(words)
        
        sets = [None]*N
        lengths = [None]*N
        
        def get_set(word):
            s = 0
            for c in word:
                s |=1 << (ord(c)-ord('a'))
            
            return s
        
        for i in range(N):
            sets[i] = get_set(words[i])
            lengths[i] = len(words[i])
            
        best = 0
        for i in range(N):
            for j in range(i+1,N):
                if (sets[i] & sets[j]) == 0:
                    #print(words[i],words[j])
                    current = lengths[i]*lengths[j]
                    best = max(best, current)
        return best