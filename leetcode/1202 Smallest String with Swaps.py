class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        N = len(s)
        
        parents = [x for x in range(N)]
        
        def ufind(x):
            if parents[x] != x:
                parents[x] = ufind(parents[x])
                
            return parents[x]
        
        def uunion(a, b):
            ua = ufind(a)
            ub = ufind(b)
            
            parents[ua] = ub
            
        for u,v in pairs:
            uunion(u,v)
            
        classes = collections.defaultdict(list)
        
        for i in range(N):
            root = ufind(i)
            classes[root].append(s[i])
            
        for key in classes.keys():
            classes[key] = collections.deque(sorted(classes[key]))
            
        ans = []
        for i in range(N):
            ans.append(classes[ufind(i)].popleft())
            
        return "".join(ans)
            