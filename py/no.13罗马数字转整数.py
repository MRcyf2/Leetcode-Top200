'''
Author: ccyfifi
Date: 2023-08-07 11:42:14
LastEditors: ccaiyf 
LastEditTime: 2023-08-07 11:42:23
Description: QQ:496357312欢迎交流

'''
class Solution:
    def romanToInt(self, s: str) -> int:
        n=len(s)
        res=0
        s1={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(n-1):
            if s1[s[i]]<s1[s[i+1]]:
                res-=s1[s[i]]
            else:
                res+=s1[s[i]]
        res+=s1[s[-1]]
        return res