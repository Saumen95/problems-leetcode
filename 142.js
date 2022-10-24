/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var detectCycle = function (head) {
  let headList = new Set();
  while (head) {
    if (headList.has(head)) {
      return head;
    }
    headList.add(head);
    head = head.next;
  }
  return null;
};
