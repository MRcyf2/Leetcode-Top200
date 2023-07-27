'''
Author: ccyfifi
Date: 2023-07-27 11:06:04
LastEditors: ccaiyf 
LastEditTime: 2023-07-27 15:12:56
Description: QQ:496357312欢迎交流

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

                
if __name__ == '__main__':
    nums=[2,7,11,15]
    target=9
    print(Solution().twoSum(nums,target))
    print('Hello World')