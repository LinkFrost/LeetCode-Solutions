# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution(object):
  def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    l3 = ListNode()
    curr = l3

    l1_curr = l1
    l2_curr = l2

    carry = False

    while l1_curr != None or l2_curr != None:
      sum = 0

      if l1_curr == None:
        sum += l2_curr.val
        l2_curr = l2_curr.next
      elif l2_curr == None:
        sum += l1_curr.val
        l1_curr = l1_curr.next
      else:
        sum += l1_curr.val + l2_curr.val
        l1_curr = l1_curr.next
        l2_curr = l2_curr.next

      if carry:
        sum += 1

      if sum > 9:
        carry = True
        sum %= 10
      else:
        carry = False

      new_node = ListNode(sum, None)
      curr.next = new_node
      curr = curr.next

      if carry:
        curr.next = ListNode(1, None)

    return l3.next
    
l1 = ListNode(val = 2)
l1.next = ListNode(val = 4)
l1.next.next = ListNode(val = 3)

l2 = ListNode(val = 5)
l2.next = ListNode(val = 6)
l2.next.next = ListNode(val = 4)

sol = Solution().addTwoNumbers(l1, l2)
print([sol.val, sol.next.val, sol.next.val])

