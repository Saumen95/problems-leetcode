class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return True

        cur = head
        stack = []
        while cur:
            stack.append(cur.val)
            cur = cur.next

        while head and stack:
            if head.val != stack.pop():
                return False
            else:
                head = head.next
        return True
