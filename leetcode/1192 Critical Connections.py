# Timothy - Tarjan
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        dis = [0]*n
        low = [0]*n
        self.time = 0
        visited = set()
        output = []
        graph = defaultdict(list)
        
        for s,t in connections:
            graph[s].append(t)
            graph[t].append(s)
            
        def dfs(cur,prev):
            visited.add(cur)
            self.time+=1
            dis[cur] = low[cur] = self.time
            
            for next in graph[cur]:
                if next not in visited:
                    dfs(next,cur)
                    low[cur] = min(low[cur], low[next])
                elif next!=prev:
                    low[cur] = min(low[cur], dis[next])
                if low[next]>dis[cur]:
                    output.append([cur,next])
                    
        dfs(0,-1)
        return output
            

# Time Limit Expired
'''
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        ans = []
        
        def dfs(node,n):
            visited.add(node)
            neighbour = []
            for i in range(n):
                if adj[node][i] == 1 and i not in visited:
                    neighbour.append(i)
            
            if neighbour:
                for neigh in neighbour:
                    dfs(neigh,n)
        
        for con in connections:
            tmp_connections = [x for x in connections if x != con]
            adj = [[0]*n for _ in range(n)]
            visited = set()
            for i in tmp_connections:
                x,y = i[0],i[1]
                adj[x][y] = 1
                adj[y][x] = 1
            
            dfs(0,n)
            if len(visited)<n:
                ans.append(con)
                
        return ans
            
'''            


# Wrong
'''
if len(connections)==1:
            return connections
        
adj = [[0]*n for _ in range(n)]
con_i = [None]*n
ans = []
for i in connections:
    x,y = i[0],i[1]
    adj[x][y] = 1
    adj[y][x] = 1
    
print(adj)
    
for i in range(n):
    con_i[i] = sum(adj[i])
    
print(con_i)
    
for i in range(n):
    if con_i[i]==1:
        for j in range(n):
            if adj[i][j] == 1:
                ans.append([i,j])
            
return ans
'''