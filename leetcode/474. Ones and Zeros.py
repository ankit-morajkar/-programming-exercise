class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        N = len(strs)
        
        zs = [0]*N
        os = [0]*N
        
        for i in range(N):
            zs[i] = strs[i].count('0')
            os[i] = strs[i].count('1')
            
        lookup = {}
            
        def get_max(index,zeros,ones):
            if index == N:
                return 0
            if (index,zeros,ones) in lookup:
                return lookup[(index,zeros,ones)]
        
            best = 0
            if zeros>=zs[index] and ones>=os[index]:
                best = get_max(index+1,zeros-zs[index],ones-os[index])+1
                
            best = max(best,get_max(index+1,zeros,ones))
            lookup[(index,zeros,ones)] = best
            return best
        
        return get_max(0,m,n)