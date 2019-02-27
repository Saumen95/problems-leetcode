class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return
        p = q = head
        r = None
        i = 0
        while q != None:
            if i != n:
                i += 1
                q = q.next
                continue
            else:
                r = p
                p = p.next
                q = q.next
        if r == None:
            return head.next
        r.next = p.next
        return head
