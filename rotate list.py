class Solution(object):
    def rotateRight(self, head, k):
        """ :type head: ListNode :type k: int :rtype: ListNode """
        if k == 0 or head == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        count = 0
        p = dummy
        while p.next:
            p = p.next
            count += 1
        p.next = head
        step = count - (k % count)
        for i in range(step):
            p = p.next
        head = p.next
        p.next = None
        return head
