class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        self.mat2 = matrix
        for col in range(len(self.mat2[0])):
            s = 0
            for row in range(len(self.mat2)):
                s += self.mat[row][col]
                self.mat2[row][col] = s
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for col in range(col1,col2+1):
            if row1==0:
                ans += self.mat2[row2][col]
            else:
                ans += (self.mat2[row2][col]-self.mat2[row1-1][col])
                
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)