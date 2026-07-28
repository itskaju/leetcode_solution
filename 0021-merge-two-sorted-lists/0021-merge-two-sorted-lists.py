class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(-1)   # temporary starter node
        tail = dummy           # tail pointer to build the merged list

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next   # move tail forward

        # attach remaining nodes
        tail.next = list1 if list1 else list2

        return dummy.next      # skip dummy, return merged head
