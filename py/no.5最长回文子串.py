'''
Author: ccaiyf 496357312@qq.com
Date: 2023-07-27 14:48:05
LastEditors: ccaiyf 496357312@qq.com
LastEditTime: 2023-07-27 14:48:49
FilePath: \Leetcode-Top200\Leetcode-Top200\py\no.5.py
Description: QQ:496357312

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#5. 最长回文子串
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==0:
            return ""
        elif len(s)==1:
            return s
        else:
            max_len=1
            max_str=s[0]
            for i in range(len(s)):
                for j in range(i+1,len(s)):
                    if s[i]==s[j]:
                        if j-i+1>max_len:
                            if s[i:j+1]==s[i:j+1][::-1]:
                                max_len=j-i+1
                                max_str=s[i:j+1]
            return max_str