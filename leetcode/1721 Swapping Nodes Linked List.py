# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        k_point = head
        for i in range(k-1):
            k_point = k_point.next
            
        fast_point = k_point
        slow_point = head
        while fast_point.next:
            fast_point = fast_point.next
            slow_point = slow_point.next
            
        slow_point.val, k_point.val = k_point.val, slow_point.val
        
        return head
            