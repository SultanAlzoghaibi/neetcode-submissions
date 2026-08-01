# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        total = 0
        mult = 0
        HEADL1 = l1
        HEADL2 = l2

        while l1 or l2:
            if l1:
                total += l1.val * (10 ** mult)
                l1 = l1.next
            if l2:
                total += l2.val * (10 ** mult)
                l2 = l2.next
            mult += 1

        print(total)
        total = str(total)[::-1]

        dummy = ListNode()
        curr = dummy
        for numC in total:
            curr.next = ListNode(int(numC))  # attach new node
            curr = curr.next  

        return dummy.next




        