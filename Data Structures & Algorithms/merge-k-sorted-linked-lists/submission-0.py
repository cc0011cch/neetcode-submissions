# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        
        chead = lists[0]
        print(type(chead))
        def mergeTwoList(l1: Optional[ListNode], l2: Optional[ListNode])-> Optional[ListNode]:
            dummy = ListNode(0)            
            thead =dummy;
            while l1 and l2:
                if l1.val< l2.val:
                    thead.next =l1
                    l1=l1.next
                else:
                    thead.next =l2
                    l2=l2.next
                thead=thead.next

            if l1: thead.next=l1
            if l2: thead.next=l2
            return dummy.next


        for i in range(1,len(lists)):
            chead=mergeTwoList(chead,lists[i])
        return chead
        