class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted = ""
        for char in s.lower():
            if char.isalnum():
                formatted += char

        return formatted == formatted[::-1]
