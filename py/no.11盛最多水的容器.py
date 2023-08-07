'''
Author: ccyfifi
Date: 2023-08-07 11:28:17
LastEditors: ccaiyf 
LastEditTime: 2023-08-07 11:28:37
Description: QQ:496357312欢迎交流

'''
from ast import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_area=0
        while left<right:
            area=min(height[left],height[right])*(right-left)
            if max_area<area:max_area=area
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area