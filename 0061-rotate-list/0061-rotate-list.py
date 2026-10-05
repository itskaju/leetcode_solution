# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head:
            return head
        # length
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

       # update 
        k = k% length

        if k == 0:
            return head

        # find new values
        new_tail = head
        for i in range(length-k-1):
            new_tail = new_tail.next

        new_head = new_tail.next
        tail.next = head
        new_tail.next = None

        return    new_head

        


        