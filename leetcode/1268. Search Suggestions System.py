class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = []
        for i in range(1,len(searchWord)+1):
            #print (searchWord[0:i])
            l = []
            for p in products:
                if p[0:i] == searchWord[0:i]:
                    l.append(p)
                    
            ans.append(sorted(l)[0:3])
            
        return ans