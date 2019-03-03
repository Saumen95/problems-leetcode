class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        cur = head

        while cur.next:

            if cur.val > cur.next.val:

                pre = dummy
                while pre.next.val < cur.next.val:
                    pre = pre.next
                m = cur.next
                cur.next = m.next
                m.next = pre.next
                pre.next = m
            else:
                cur = cur.next

        return dummy.next
