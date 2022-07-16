class Solution:
    def findPaths(self, R: int, C: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9+7
        
        board = [[0]*C for _ in range(R)]
        
        board[startRow][startColumn] = 1
        total = 0
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        for _ in range(maxMove):
            next_board = [[0]*C for _ in range(R)]
            
            for x in range(R):
                for y in range(C):
                    for dx, dy in directions:
                        nx,ny = x+dx, y+dy
                        
                        if 0<=nx<R and 0<=ny<C:
                            next_board[nx][ny] += board[x][y]
                            next_board[nx][ny]%= MOD
                        else:
                            total += board[x][y]
                            total %= MOD
                            
            board = next_board
                
        return total%MOD