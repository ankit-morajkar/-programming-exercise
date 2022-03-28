class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        boats = 0
        l,r = 0, len(people)-1
        while l<=r:
            boats +=1
            remain_cap = limit - people[r]
            r -=1
            if l<=r and remain_cap>=people[l]:
                l +=1
                
        return boats