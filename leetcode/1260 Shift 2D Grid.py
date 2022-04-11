class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        rows = len(grid)
        cols = len(grid[0])
        flat_list = deque()
        for sublist in grid:
            for ele in sublist:
                flat_list.append(ele)
                
        flat_list.rotate(k)
        
        ans = []
        
        for i in range(rows):
            ans.append(list(itertools.islice(flat_list, i*cols, (i+1)*cols)))
            
        return ans