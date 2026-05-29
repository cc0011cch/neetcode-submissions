# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        lmap=defaultdict(int)
        while head is not None:
            lmap[head]+=1
            if lmap[head] >1: return True
            head=head.next
        return False  