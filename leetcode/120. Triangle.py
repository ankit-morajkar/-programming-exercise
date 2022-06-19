class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        levels = len(triangle)
        dp = [[triangle[0][0]]]
        
        for level in range(1, levels):
            best_lev = []
            for i in range(level+1):
                if i == 0:
                    best_lev.append(dp[level-1][i]+triangle[level][i])
                elif i == level:
                    best_lev.append(dp[level-1][i-1]+triangle[level][i])
                else:
                    best_lev.append(min(dp[level-1][i-1]+triangle[level][i], dp[level-1][i]+triangle[level][i]))
                
            dp.append(best_lev)
                    
        return min(dp[levels-1])