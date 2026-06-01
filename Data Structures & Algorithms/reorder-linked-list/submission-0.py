# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None or head.next.next is None: return 

        slrptr=head
        farptr=head

        while farptr and farptr.next:
            slrptr=slrptr.next
            farptr=farptr.next.next
        sec_head=slrptr.next
        slrptr.next =None


        def reversList(shead: Optional[ListNode]) -> Optional[ListNode]:
            if shead is None or shead.next is None: return shead
            revList =reversList(shead.next)
            shead.next.next=shead
            shead.next=None
            return revList

        sec_head = reversList(sec_head)
        chead=head
        while chead and sec_head:
            tmp1= chead.next
            tmp2= sec_head.next            
            chead.next = sec_head
            sec_head.next=tmp1
            chead=tmp1
            sec_head=tmp2

