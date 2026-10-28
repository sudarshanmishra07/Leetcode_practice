class Solution:
    def longestUniqueSubstr(self, s):
        if len(s) == 0 or len(s) == 1:
                return len(s)
        res = 0
        vis = [False] * 26
        left = 0
        right = 0
        while right < len(s):
            while vis[ord(s[right]) - ord('a')] == True:    # If character is repeated, move left pointer marking
                vis[ord(s[left]) - ord('a')] = False        # visited characters as false until the repeating
                left += 1                                   # character is no longer part of the current window
                
            vis[ord(s[right]) - ord('a')] = True            # The length of the current window (right - left + 1)
            res = max(res, (right - left + 1))              # is calculated and answer is updated accordingly.
            right += 1
        return res
