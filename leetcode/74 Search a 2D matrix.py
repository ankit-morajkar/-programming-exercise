class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        t = 0
        b = len(matrix)-1
        l = 0
        r = len(matrix[0])-1
        
        while t<b:
            mr = int(math.ceil((t+b)/2.0))
            if target >= matrix[mr][0]:
                t = mr
            else:
                b = mr-1
                
            if mr<b:
                if target < matrix[mr+1][0]:
                    b = mr
                      
        while l <= r:
            mc = int(math.floor((l+r)/2))
            print(l,mc,r,matrix[t][mc])
            if target == matrix[t][mc]:
                return True
            if l == r:
                return False
            if target > matrix[t][mc]:
                l = mc+1
            else:
                r = mc-1