class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visited = set()
        q = deque()
        dirs = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(-1,-1),(1,-1)]
        
        if grid[0][0] == 0:
            q.append((1,(0,0)))
            visited.add((0,0))
            
        while q:
            steps, tmp = q.popleft()
            r,c = tmp[0], tmp[1]
            if (r,c) == (N-1,N-1):
                return steps
            for i,j in dirs:
                new_r,new_c = r+i,c+j
                if 0<=new_r<N and 0<=new_c<N and grid[new_r][new_c]==0 and(new_r,new_c) not in visited:
                    q.append((steps+1,(new_r,new_c)))
                    visited.add((new_r,new_c))
                    
        return -1
        