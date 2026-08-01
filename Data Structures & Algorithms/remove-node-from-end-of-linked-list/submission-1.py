# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head.next == None: 
            head = None
            return head

                

        curr = head

        nthNode = head
        nthNodePrev = ListNode()
        nthNodeNext = head.next

        for _ in range(n):
            curr = curr.next
           

        if not curr:
            return head.next


        while curr:
            curr = curr.next
            nthNodePrev = nthNode
            nthNode = nthNode.next
            nthNodeNext = nthNodeNext.next

        nthNodePrev.next = nthNodeNext

        return head

    
        
