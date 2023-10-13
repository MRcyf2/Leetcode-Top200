'''
Author: ccyfifi
Date: 2023-08-14 17:12:07
LastEditors: ccaiyf 
LastEditTime: 2023-08-15 15:27:23
Description: QQ:496357312欢迎交流
242. 有效的字母异位词


'''
#2236. 判断根结点是否等于子结点之和

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        a=root.val
        b=root.left.val
        c=root.right.val
        if a==b+c:
            return True
        else:
            return False
