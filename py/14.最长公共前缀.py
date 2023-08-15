'''
Author: ccyfifi
Date: 2023-08-15 10:42:03
LastEditors: ccaiyf 
LastEditTime: 2023-08-15 10:44:14
Description: QQ:496357312欢迎交流

'''


from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=''
        s=strs[0]
        for ss in strs:
            for i in range(len(s)):
                if i<len(ss) and ss[i]==s[i]:
                    continue
                else:
                    s=s[:i]
                    break
        return s
