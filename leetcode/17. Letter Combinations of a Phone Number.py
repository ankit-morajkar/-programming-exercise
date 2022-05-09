class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = dict()
        mapping['2'] = ['a','b','c']
        mapping['3'] = ['d','e','f']
        mapping['4'] = ['g','h','i']
        mapping['5'] = ['j','k','l']
        mapping['6'] = ['m','n','o']
        mapping['7'] = ['p','q','r','s']
        mapping['8'] = ['t','u','v']
        mapping['9'] = ['w','x','y','z']
        
        ans = []
        if len(digits)==0:
            return ans
        
        def dfs(digits, string):
            nonlocal ans
            if len(digits) == 1:
                for ele in mapping[digits]:
                    ans.append(string+ele)
            else:
                for s in mapping[digits[0]]:
                    #print(digits[1:],string+s)
                    dfs(digits[1:],string+s)
                    
        dfs(digits, "")
        return ans