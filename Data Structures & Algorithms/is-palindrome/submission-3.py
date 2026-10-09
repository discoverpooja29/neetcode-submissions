import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        revStr = ''.join(char.lower() for char in s if char.isalnum())
        
        return revStr == revStr[::-1]

        
