class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        temp_board = []
                
        for r in range(len(board)):
            temp = []
            for c in range(len(board[0])):
                temp.append(board[r][c])
                
            temp_board.append(temp)
        
        n = len(board[0])
        m = len(board)
        directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        
        def neighbour_count(i,j):
            neighbours = 0
            for x_step, y_step in directions:
                ny = i+y_step
                nx = j+x_step
                if nx >= 0 and ny >= 0 and nx < n and ny < m:
                    if board[ny][nx]==1:
                        neighbours = neighbours +  1
                        
            return neighbours
        
        for i in range(m):
            for j in range(n):
                neighbour_v = neighbour_count(i,j)
                if neighbour_v<2:
                    temp_board[i][j] = 0
                elif neighbour_v==3:
                    temp_board[i][j] = 1
                elif neighbour_v>3:
                    temp_board[i][j] = 0
                    
        for r in range(len(temp_board)):
            for c in range(len(temp_board[0])):
                board[r][c] = temp_board[r][c]
                
        