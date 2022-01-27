# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        
        i = 0
        
        curr = head
        
        n = 1
        while curr.next:
            curr = curr.next
            n += 1

        curr = head
        
        while curr.next and i != n//2:
            stack.append(curr.val)
            curr = curr.next
            i += 1
            
        twin_sums = []

        while curr:
            twin_sums.append(curr.val + stack.pop())
            curr = curr.next
            
        return max(twin_sums)