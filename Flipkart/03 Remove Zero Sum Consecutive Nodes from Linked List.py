# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        sum2node = {0:dummy}
        currSum = 0
        while head:
            currSum += head.val
            if currSum in sum2node:
                # remove
                remove = sum2node[currSum].next
                removeTotal = currSum
                while remove != head:
                    removeTotal += remove.val
                    sum2node.pop(removeTotal)
                    remove = remove.next

                # change link
                sum2node[currSum].next = head.next

            else:
                sum2node[currSum] = head

            head = head.next

        return dummy.next
