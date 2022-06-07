class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = 0
        x = m
        b = 0
        while a<(m+n) and b<n:
            #print(a,b,nums1)
            if a==x:
                nums1[a]=nums2[b]
                x+=1
                a+=1
                b+=1
            elif nums1[a]<=nums2[b]:
                a += 1
            elif nums1[a]>nums2[b]:
                y = x+1
                while x>a:
                    nums1[x]=nums1[x-1]
                    x-=1
                x=y
                nums1[a]=nums2[b]
                b+=1
            