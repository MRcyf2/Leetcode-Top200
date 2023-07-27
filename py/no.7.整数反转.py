'''
Author: ccyfifi
Date: 2023-07-27 15:09:29
LastEditors: ccaiyf 
LastEditTime: 2023-07-27 15:13:36
Description: QQ:496357312欢迎交流

'''

#7. 整数反转

class Solution:
    def reverse(self, x: int) -> int:
        carry = 1 if x >= 0 else -1
        x = abs(x)
        res = 0
        while x:
            res = res * 10 + x % 10
            x //= 10
        res *= carry
        return res if -2 ** 31 <= res <= 2 ** 31 - 1 else 0
    