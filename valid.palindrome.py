class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch.isalnum():
                stack.append(ch.lower())
        for ch in s:
            if ch.isalnum():
                if ch.lower() != stack.pop():
                    return False
        return True