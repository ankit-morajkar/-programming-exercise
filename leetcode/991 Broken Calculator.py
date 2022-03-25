class Solution(object):
    count = 0
    def brokenCalc(self, startValue, target):
        """
        :type startValue: int
        :type target: int
        :rtype: int
        """
        count = 0
        while(target>startValue):
            count += 1
            if target % 2 == 1:
                target += 1
                
            else:
                target = target/2
                
                
        return count + startValue - target