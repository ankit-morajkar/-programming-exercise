class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        lang = dict()
        
        for i in range(len(order)):
            lang[order[i]] = i
            
        for x in range(len(words)-1):
            w1, w2 = words[x], words[x+1]
            N = min(len(w1), len(w2))
            for i in range(N):
                if lang[w1[i]]>lang[w2[i]]:
                    return False
                if lang[w1[i]]<lang[w2[i]]:
                    break

            if len(w1)>len(w2) and lang[w1[i]]==lang[w2[i]] :
                return False
        
        return True