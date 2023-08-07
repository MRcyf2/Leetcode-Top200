'''
Author: ccyfifi
Date: 2023-08-07 10:28:08
LastEditors: ccaiyf 
LastEditTime: 2023-08-07 10:28:18
Description: QQ:496357312欢迎交流

'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]