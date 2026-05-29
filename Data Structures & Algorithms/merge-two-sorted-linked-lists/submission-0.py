# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None : return list1
        if list1 is None : return list2
        if list2 is None : return list1
        nlist=None
        tail=None
        while list1 and list2 :
            if list1.val < list2.val:
                current =list1
                list1 =list1.next
            else:
                current=list2
                list2 = list2.next
            if nlist is None: 
                nlist =current
                tail=current
            else:
                tail.next=current
                tail=tail.next
        tail.next= list1 if list1 else list2
        return nlist