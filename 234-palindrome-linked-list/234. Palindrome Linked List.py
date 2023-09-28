# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse_list(cur_head):
            prev = None
            while cur_head:
                next_ref = cur_head.next
                cur_head.next = prev
                prev = cur_head
                cur_head = next_ref
            return prev
        
        # find middle node
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is the middle node
        # right is the new head of reversed list
        right = reverse_list(slow)
        while head and right:
            if head.val != right.val:
                return False
            head = head.next
            right = right.next
        return True
            
        