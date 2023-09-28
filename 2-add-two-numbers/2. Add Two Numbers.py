# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # we can just sum them up using carry
        # (we don't need to reverse the input lists)
        dummy = ListNode()
        curr = dummy
        curr_carry = 0
        while l1 or l2:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            curr_carry, decimal = divmod(curr_carry+sum, 10)
            curr.next = ListNode(decimal)
            curr = curr.next
        if curr_carry != 0:
            curr.next = ListNode(curr_carry)
        return dummy.next
