class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        m = len(mat)
        n = len(mat[0])
        row_score = {}
        for i in range(m):
            row_score[i] = mat[i].count(1)+float(i/10**(math.floor(math.log(m,10))+1))
            
        sorted_score = sorted(row_score.items(), key=operator.itemgetter(1))
        ans = []
        for i in range(k):
            ans.append(sorted_score[i][0])
        
        return ans