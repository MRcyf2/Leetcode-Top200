'''
Author: ccyfifi
Date: 2023-08-14 17:12:07
LastEditors: ccaiyf 
LastEditTime: 2023-08-14 17:17:12
Description: QQ:496357312欢迎交流
242. 有效的字母异位词


'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)