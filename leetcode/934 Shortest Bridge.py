class Solution(object):
    def shortestBridge(self, grid):
        N = len(grid)
        #print(N)
        
        def invalid_coordinates(x,y):
            return x<0 or y<0 or x==N or y==N
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        visit = set()
        
        def dfs(x,y):
            if invalid_coordinates(x,y) or (x,y) in visit or grid[x][y]==0:
                return
            visit.add((x,y))
            for dr, dc in directions:
                dfs(x+dr, y+dc)
            
        def bfs():
            res, q = 0, deque(visit)
            while q:
                for i in range(len(q)):
                    x,y = q.popleft()
                    for dr, dc in directions:
                        curR, curC = x+dr, y+dc
                        if invalid_coordinates(curR,curC) or (curR,curC) in visit:
                            continue
                        if grid[curR][curC]:
                            return res
                        q.append([curR,curC])
                        visit.add((curR,curC))
                res +=1
                  
        for i in range(N):
            for j in range(N):
                if grid[i][j]==1:
                    dfs(i,j)
                    return bfs()