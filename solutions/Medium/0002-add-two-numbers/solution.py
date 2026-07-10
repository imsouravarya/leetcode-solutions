# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node acts as the placeholder for the start of our result list
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Keep looping as long as there are digits to add or a carry left over
        while l1 or l2 or carry:
            # Extract values if nodes exist, otherwise use 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate total sum for this position and the new carry
            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            
            # Create the next node with the single-digit result
            current.next = ListNode(total_sum % 10)
            current = current.next
            
            # Move to the next nodes in the input lists if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return dummy_head.next