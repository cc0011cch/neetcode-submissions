/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
#include <memory>
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
//iterative
/*        decltype(head) prev{nullptr};
        decltype(head) curr{head};
        while (curr){
            decltype(head) tmp= curr->next;
            curr->next=prev;
            prev=curr;
            curr =tmp;
        }
        return prev;*/
//recursive
        if (!head  || !head->next) return head;
        decltype(head) rehead = reverseList(head->next);
        head->next->next=head;
        head->next= static_cast<ListNode*>(nullptr);
        return rehead;
    }
};
