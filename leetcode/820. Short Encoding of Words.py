class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        ans = 0
        has = False
        word_set = set(words)
        words = list(word_set)
        words.sort(key=lambda s: -len(s))
        for i in range(len(words)):
            has = False
            for j in range(i):
                if words[j].endswith(words[i]) and i!=j:
                    has = True
                    break
                    
            if has:
                continue
            else:
                ans += len(words[i])+1
                
        return ans