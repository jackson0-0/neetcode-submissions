class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l < r: 
            while l < r and not s[l].isalnum():
                left += 1 
            while l < r and not s[r].isalnum(): 
                left -= 1
            if s[l] != s[r]:
                return False 