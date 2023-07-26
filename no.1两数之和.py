'''
Author: ccaiyf 496357312@qq.com
Date: 2023-07-26 14:26:59
LastEditors: ccaiyf 496357312@qq.com
LastEditTime: 2023-07-26 14:41:50
Description: QQ:496357312

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''



from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []
