
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda e:(e[0],-e[1]))
        INF = 10**10
        
        best = [-INF]
        
        for x,y in envelopes:
            index = bisect.bisect_left(best,y)
            
            if index>=len(best):
                best.append(y)
            else:
                best[index] = y
            
        return len(best)-1
        


# 'Ankit Solution: TLE'
# class Solution:
#     def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
#         N = len(envelopes)
#         adj = [[0]*N for i in range(N)]
#         ans = 0
#         dp = {}
        
#         for i,p in enumerate(envelopes):
#             for j,q in enumerate(envelopes):
#                 if q[0]<p[0] and q[1]<p[1]:
#                     adj[j][i] = 1
                    
                    
#         def dfs(index, depth):
#             mx = 0
#             neighbours = adj[index]
#             if sum(neighbours) == 0:
#                 return depth
            
#             for y,neigh in enumerate(neighbours):
#                 if neigh == 1:
#                     if y in dp:
#                         mx = max(mx,dp[y])
#                     else:
#                         mx = max(mx,dfs(y,depth+1)) 
                
#             return mx
                    
#         for x,e in enumerate(envelopes):
#             ans = max(ans, dfs(x,1))
#             dp[x] = ans
            
#         return ans