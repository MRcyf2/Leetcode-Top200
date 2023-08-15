'''
Author: ccyfifi
Date: 2023-08-15 11:04:34
LastEditors: ccaiyf 
LastEditTime: 2023-08-15 11:16:05
Description: QQ:496357312欢迎交流
17. 电话号码的字母组合

'''
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res=[]
        lens=len(digits)
        if lens==0:
            return res
        def dfs(i):#i表示当前遍历到的数字的下标
            if i==lens:
                res.append(''.join(tmp))#这句话的意思是，当i=lens时，说明已经遍历完了所有的数字，此时tmp中存储的就是一种结果，将其加入res中
                return
            for c in table[digits[i]]:
                tmp.append(c)
                dfs(i+1)
                tmp.pop()
        tmp=[]
        dfs(0)
        return res
    
# 当digits='23'时，dfs(0)的执行过程如下：
# tmp=[]
# dfs(0)
#     tmp=['a']
#     dfs(1)
#         tmp=['a','d']
#         dfs(2)
#             res=['ad']
#         tmp=['a','e']
#         dfs(2)
#             res=['ad','ae']
#         tmp=['a','f']
#         dfs(2)
#             res=['ad','ae','af']    
#     tmp=['b']
#     dfs(1)  