# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        ptr = head
        rem = 0
        prev = ListNode
        while l1 and l2:
            sum = l1.val + l2.val + rem
            rem = 0
            if sum >= 10:
                sum = sum - 10
                rem += 1
            ptr.val = sum
            l1 = l1.next
            l2 = l2.next
            ptr.next = ListNode()
            prev = ptr
            ptr = ptr.next
        longest = l1 if l2 == None else l2
        while longest:
            sum = longest.val + rem
            rem = 0
            if sum >= 10:
                sum = sum - 10
                rem += 1
            ptr.val = sum
            prev = ptr
            ptr.next = ListNode()
            ptr = ptr.next
            longest = longest.next
        if rem != 0:
            ptr.val = rem
        else:
            prev.next = None
        return head