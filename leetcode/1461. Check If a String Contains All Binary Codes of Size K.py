
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        l = 0
        r = k
        visited = set()
        while r<=len(s):
            if s[l:r] not in visited:
                visited.add(s[l:r])
                
            l +=1
            r +=1
        
        if len(visited) == 2**k:
            return True
        return False

# Brute Force
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        def bfs(bit,i,s):
            #print(bit,i,s)
            if i<=k:
                if bit in s:
                    #print("Bit in S")
                    if bfs('0'+bit,i+1,s) and bfs('1'+bit,i+1,s):
                        return True
                    else:
                        return False
                else:
                    #print("Bit not in S")
                    return False
            else:
                return True
            
        if bfs('0',1,s) and bfs('1',1,s):
            return True
        return False
                
            
            