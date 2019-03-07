class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return head
        p = ListNode(-1)
        p.next = head
        slow = p
        while head != None:
            if head.val == val:
                slow.next = head.next
            else:
                slow = slow.next
            head = head.next
        return p.next
