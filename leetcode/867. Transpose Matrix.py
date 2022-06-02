class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        M = len(matrix)
        N = len(matrix[0])
        ans = [[None]*M for _ in range(N)]
        
        for i in range(N):
            for j in range(M):
                ans[i][j] = matrix[j][i]
                
        return ans