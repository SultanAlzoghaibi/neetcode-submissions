# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        l1 = head
        l2 = prev
        
        while  l1 and l2:
            tmp1 = l1.next
            tmp2 = l2.next
            l1.next = l2

            if tmp1 is None:
                break  # If original list had odd length
            l2.next = tmp1
            l1 = tmp1
            l2 = tmp2

            




