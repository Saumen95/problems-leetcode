class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = None
        while head:
            nextNode = head.next
            head.next = newHead
            newHead = head
            head = nextNode
        return newHead
