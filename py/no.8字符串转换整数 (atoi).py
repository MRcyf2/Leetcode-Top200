'''
Author: ccyfifi
Date: 2023-08-07 10:24:14
LastEditors: ccaiyf 
LastEditTime: 2023-08-07 10:26:13
Description: QQ:496357312欢迎交流

'''
class Solution:
    def myAtoi(self, s: str) -> int:
        length = len(s)
        flag=1
        res=0
        i=0
        while i<length and s[i]==' ':
            i+=1
        if i<length and s[i]=='-':
            flag=-1
            i+=1
        elif i<length and s[i]=='+':
            i+=1
        while i<length and s[i].isdigit(): 
            res=res*10+int(s[i])
            i+=1
        res*=flag
        if res>2**31-1:
            res=2**31-1
        elif res<-2**31:
            res=-2**31
        return res
    