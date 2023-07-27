# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#2. 两数相加

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum=0
        carry=0
        head=ListNode()
        cur=head
        while l1 or l2 or carry:
            sum=0
            if l1:
                sum+=l1.val
                l1=l1.next
            if l2:
                sum+=l2.val
                l2=l2.next
            sum+=carry
            carry=sum//10
            cur.next=ListNode(sum%10)
            cur=cur.next
        return head.next
    