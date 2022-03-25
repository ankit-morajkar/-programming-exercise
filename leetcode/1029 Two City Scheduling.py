class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        sumA = 0
        index_diff = []
        for person_index in range(len(costs)):
            sumA = sumA + costs[person_index][0]
            index_diff.append(costs[person_index][1] - costs[person_index][0])
        
        index_diff.sort()
        for i in range(len(costs)/2):
            sumA = sumA + index_diff[i]
            
        return sumA