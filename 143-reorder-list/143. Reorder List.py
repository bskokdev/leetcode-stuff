# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head) -> ListNode:
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return
        # move slow and fast pointer to their positions
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half -> rev_slow will be at the end
        rev_slow = self.reverse(slow.next)    
        slow.next = None

        # update pointers
        fast = head
        while rev_slow:
            nxt = fast.next
            fast.next = rev_slow
            fast = rev_slow
            rev_slow = nxt
