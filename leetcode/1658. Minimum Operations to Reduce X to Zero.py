class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        if sum(nums)<target:
            return -1
        
        suffix_seen = {}
        suffix_seen[0] = 0
        
        current = 0
        for i,x in enumerate(reversed(nums),1):
            current +=x
            suffix_seen[current] = i
            
        INF = 10**20
        best = INF
        if target in suffix_seen:
            best = min(best, suffix_seen[target])
            
        current = 0
        for i,x in enumerate(nums,1):
            current +=x
            if target - current in suffix_seen:
                best = min(best, suffix_seen[target-current]+i)
                
        if best == INF:
            return -1
        return best