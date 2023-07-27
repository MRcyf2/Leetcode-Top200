#3. 无重复字符的最长子串
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lens=0
        max_len=0
        left=0
        right=0
        for i in range(len(s)):
            for j in range(left,right):
                if s[i]==s[j]:
                    left=j+1
                    break
            right+=1
            lens=right-left
            if lens>max_len:
                max_len=lens

        return max_len