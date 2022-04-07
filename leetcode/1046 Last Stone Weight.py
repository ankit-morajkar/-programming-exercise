class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        while(len(stones)>1):
            stones.sort(reverse=True)
            s1 = stones.pop(0)
            s2 = stones.pop(0)
            if s1 == s2:
                pass
            else:
                stones.append(abs(s1-s2))
                
        if len(stones)==1:
            return stones.pop()
        else:
            return 0
        