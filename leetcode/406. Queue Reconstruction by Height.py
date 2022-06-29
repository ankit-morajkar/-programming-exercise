class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda p: (-p[0],p[1]))
        
        # print(people)
        ans = []
        for height, k in people:
            # print(height,k)
            ans.insert(k,[height,k])
            # print(ans)
            
        return ans