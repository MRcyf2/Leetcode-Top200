'''
Author: ccyfifi
Date: 2023-07-28 10:40:51
LastEditors: ccaiyf 
LastEditTime: 2023-07-28 15:42:35
Description: QQ:496357312欢迎交流

'''
#kmp
def kmp(s):
    nxt, j = [-1], -1
    for i in range(len(s)):
        while j >= 0 and s[i] != s[j]:
            j = nxt[j]
        j += 1
        nxt.append(j)
    return nxt     # nxt[i]:i-1结尾的最大真前缀长度


#############################################################

#manacher
def manacher(s):
    s = '#' + '#'.join(s) + '#'
    n=len(s)
    A,B=[],[1]*n  #A:回文半径 B:回文半径个数
    mid,r=0,0   #mid:最大回文半径中心 r:最大回文半径右边界
    for i in range(n):
        a=min(A[2*mid-i],r-i) if r>i else 0   #a:当前回文半径
        while i-a>=0 and i+a<n-1 and s[i-a-1]==s[i+a+1]:
            a+=1
            B[i+a]=max(B[i+a],a*2+1)
        A.append(a)
        if i+a>r:
            mid,r=i,i+a
    return B[1:-1]#回文半径个数