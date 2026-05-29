# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None: return False
        slptr=head
        faptr=head.next
        while slptr!=faptr:
            if faptr ==None or faptr.next ==None: return False
            slptr=slptr.next
            faptr=faptr.next.next
        return True
 #       lmap=defaultdict(int)
 #       while head is not None:
 #           lmap[head]+=1
 #           if lmap[head] >1: return True
 #           head=head.next
 #       return False  