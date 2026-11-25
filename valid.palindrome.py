class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []                          # blank stack
        for ch in s:
            if ch.isalnum():                #check if character is alphanumeric
                stack.append(ch.lower())    #store lowercase character
        for ch in s:
            if ch.isalnum():
                if ch.lower() != stack.pop():   #compare with reversed character
                    return False            #not a palindrome
        return True                         #string is palindrome