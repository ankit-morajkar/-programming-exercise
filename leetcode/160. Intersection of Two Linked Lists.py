# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seta = []
        setb = []
        #print(headA)
        
        while headA:
            seta.append(headA)
            headA = headA.next
            
        while headB:
            setb.append(headB)
            headB = headB.next
        
        a = len(seta)-1
        b = len(setb)-1
        while seta[a]==setb[b] and a>=0 and b>=0:
            a -= 1
            b -= 1
        
        if a == len(seta)-1:
            return None
        
        if seta[a+1]==setb[b+1]:
            return seta[a+1]
        