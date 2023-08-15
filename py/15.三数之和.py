'''
Author: ccyfifi
Date: 2023-08-15 10:49:13
LastEditors: ccaiyf 
LastEditTime: 2023-08-15 10:54:35
Description: QQ:496357312欢迎交流

'''
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        for i in range(n-2):
            if nums[i]>0:
                break
            if nums[i]==nums[i-1] and i>0:#去重,i>0是为了防止i-1越界
                continue
            l=i+1
            r=n-1
            while l<r:
                if nums[i]+nums[l]+nums[r]==0:
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                elif nums[i]+nums[l]+nums[r]<0:
                    l+=1
                else:
                    r-=1
        return res