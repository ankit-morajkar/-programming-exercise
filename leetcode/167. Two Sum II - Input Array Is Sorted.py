class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        N = len(numbers)
        
        for i1 in range(N):
            if i1>0:
                if numbers[i1-1] == numbers[i1]:
                    continue
            for i2 in range(i1+1,N):
                if i2>i1+1:
                    if numbers[i2-1]==numbers[i2]:
                        continue
                add = numbers[i1]+numbers[i2]
                if add>target:
                    break
                elif add == target:
                    return [i1+1,i2+1]