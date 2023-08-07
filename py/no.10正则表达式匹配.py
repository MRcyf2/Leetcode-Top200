'''
Author: ccyfifi
Date: 2023-08-07 10:29:29
LastEditors: ccaiyf 
LastEditTime: 2023-08-07 11:16:27
Description: QQ:496357312欢迎交流

'''

'''
第一种情况：s[i]==p[j] or p[j]=='.'，则dp[i][j]=dp[i-1][j-1]
第二种情况：p[j]=='*'，则分为两种情况
    1. *匹配0次，dp[i][j]=dp[i][j-2]     eg: s='ab',p='abc*'
    2. *匹配多次，dp[i][j]=dp[i-1][j] and (s[i]==p[j-1] or p[j-1]=='.')   eg: s='ab',p='.*'
    3. *匹配1次，dp[i][j]=dp[i-1][j-1] and (s[i]==p[j-1] or p[j-1]=='.')        eg: s='ab',p='.*b'
    
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len=len(s)
        p_len=len(p)
        dp=[[False]*(p_len+1) for _ in range(s_len+1)]#dp[i][j]表示s的前i个字符和p的前j个字符是否匹配
        dp[0][0]=True
        for j in range(1,p_len+1):
            if p[j-1]=='*':
                dp[0][j]=dp[0][j-2]
        for i in range(1,s_len+1):
            for j in range(1,p_len+1):
                if s[i-1]==p[j-1] or p[j-1]=='.':
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j]=dp[i][j-2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.')) or (dp[i - 1][j - 1] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))


        return dp[-1][-1]