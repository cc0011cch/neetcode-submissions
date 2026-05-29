# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#interative  
#        prev = None
#        curr = head
#        while curr:
#            tmp= curr.next
#            curr.next =prev
#            prev = curr
#            curr =tmp
#        return prev      
#recursive
        if head is None or head.next is None: return head

        revhead =self.reverseList(head.next)
        head.next.next=head #make it to circle.. by removing None
        head.next =None
        return revhead
