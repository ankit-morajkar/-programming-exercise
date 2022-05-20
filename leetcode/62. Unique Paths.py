class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dirs = [(0,1),(1,0)]
        dp = {}
        dp[(m-1,n-1)]=1
        
        def dfs(old_x,old_y):
            if (old_x,old_y) in dp:
                return dp[(old_x,old_y)]
            
            val = 0
            for r,c in dirs:
                x,y = old_x+r,old_y+c
                if x < m and y < n:
                    val = val + dfs(x,y)
                    
            dp[(old_x,old_y)] = val
            return val
        
        
        return dfs(0,0)
#         for i in range(m):
#             t = []
#             for j in range(n):
#                 t.append(dp[(i,j)])
                
#             print(t)