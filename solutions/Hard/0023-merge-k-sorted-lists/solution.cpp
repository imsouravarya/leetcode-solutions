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
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty()) return nullptr;

        ListNode dummy;
        ListNode* tail = &dummy;

        for (ListNode* head : lists){
            if (!head) continue;

            tail->next = head;
            while (tail->next) tail = tail->next;}

            vector<int> vals;
            for (ListNode* curr = dummy.next; curr != nullptr; curr = curr->next){vals.push_back(curr->val);

        }
        sort(vals.begin(), vals.end());

        int i = 0;
        for (ListNode* curr = dummy.next; curr != nullptr; curr = curr->next){
            curr->val = vals[i++];
        }

        return dummy.next;

    }
};