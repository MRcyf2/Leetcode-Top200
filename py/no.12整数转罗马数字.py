'''
Author: ccyfifi
Date: 2023-08-07 11:35:56
LastEditors: ccaiyf 
LastEditTime: 2023-08-07 11:41:00
Description: QQ:496357312欢迎交流

'''






    
class Solution:
    def intToRoman(self, num: int) -> str:
        
        n = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        m = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        res = ''
        
        for i in range(13):
            while num >= n[i]:
                num -= n[i]
                res += m[i]
                
        return res
