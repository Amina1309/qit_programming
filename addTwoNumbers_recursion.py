# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def addLists(x, y, c=0):
            z = x.val + y.val + c
            c = z // 10
            z = z % 10

            x = x.next
            y = y.next
            if (x is None) and (y is not None):
                x = ListNode(0, None)
            elif (x is not None) and (y is None):
                y = ListNode(0, None)
            elif (x is None) and (y is None):
                if c > 0:
                    x = ListNode(0, None)
                    y = ListNode(0, None)
                else:

                    return ListNode(z, None)

            return ListNode(z, addLists(x, y, c))

        return addLists(l1, l2)
