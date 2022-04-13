class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for x in range(n)] for y in range(n)]
        
        cnt = 1
        for layer in range(int((n+1)/2)):
            # direction 1 - traverse from left to right
            for ptr in range(layer, n-layer):
                #print(layer,ptr, cnt)
                ans[layer][ptr] = cnt
                #print(ans)
                cnt += 1
                
            for ptr in range(layer+1, n-layer):
                #print(ptr, n-layer-1, cnt)
                ans[ptr][n-layer-1] = cnt
                #print(ans)
                cnt += 1
                
            for ptr in range(n-layer-2, layer-1, -1):
                #print(n-layer-1, ptr, cnt)
                ans[n-layer-1][ptr] = cnt
                #print(ans)
                cnt += 1
                
            for ptr in range(n-layer-2, layer, -1):
                #print(ptr, layer, cnt)
                ans[ptr][layer] = cnt
                #print(ans)
                cnt += 1
        
        #print(ans)
        return ans
            
        