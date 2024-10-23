# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def listNodeToStr(list_node):
            o = ""
            x = list_node
            while x is not None:
                o += str(x.val)
                x = x.next

            return o

        def strToReversedListNode(s):
            o = None
            for x in s:
                o = ListNode(int(x), o)

            return o

        a = listNodeToStr(l1)
        b = listNodeToStr(l2)
        s = str(int(a[::-1]) + int(b[::-1]))

        return strToReversedListNode(s)
