'''
Author: ccyfifi
Date: 2023-08-15 10:57:52
LastEditors: ccaiyf 
LastEditTime: 2023-08-15 10:58:02
Description: QQ:496357312欢迎交流

'''
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        res=nums[0]+nums[1]+nums[2]
        if n==3:
            return res
        for i in range(n-2):
            l=i+1
            r=n-1
            while l<r:
                t=nums[i]+nums[l]+nums[r]
                if abs(t-target)<abs(res-target):
                    res=t
                if t==target:
                    return target
                elif t<target:
                    l+=1
                else:
                    r-=1
        return res