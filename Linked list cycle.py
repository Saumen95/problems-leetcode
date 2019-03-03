
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head  # start iterating

        while slow != None and fast != None:
            if slow.next == None or fast.next == None:  # pointing next node
                return False
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # if there is cycle
                return True
        return False
