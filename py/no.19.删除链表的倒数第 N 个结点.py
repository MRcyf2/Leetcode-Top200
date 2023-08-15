'''
Author: ccyfifi
Date: 2023-08-15 11:27:40
LastEditors: ccaiyf 
LastEditTime: 2023-08-15 11:36:13
Description: QQ:496357312欢迎交流

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next=slow.next.next #左指针的下一个节点就是倒数第 n 个节点
        return head
        
    
