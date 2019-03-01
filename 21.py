class Solution(object):
    def mergeTwoLists(self, l1, l2):
        ret = ListNode(0)
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        if l1.val < l2.val:
            ret = l1
            ret.next = self.mergeTwoLists(l1.next, l2)
        else:
            ret = l2
            ret.next = self.mergeTwoLists(l2.next, l1)

        return ret
