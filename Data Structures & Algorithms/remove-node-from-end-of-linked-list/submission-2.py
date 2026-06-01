# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n>=1 and head.next is None: return
        
        sptr=head
        eptr=head
        N=0

        while N<n+1:
            if eptr is None:
                sptr=sptr.next
                return sptr

            eptr=eptr.next
            N+=1
            
        while eptr:
            eptr=eptr.next
            sptr=sptr.next

        print(sptr.val)
        sptr.next=sptr.next.next
        return head