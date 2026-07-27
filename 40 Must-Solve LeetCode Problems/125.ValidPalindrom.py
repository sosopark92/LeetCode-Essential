# A phrase is a palindrome if, 
# after converting all uppercase letters into lowercase letters 
# and removing all non-alphanumeric characters, 
# it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert the string to lowercase and filter out non-alphanumeric characters
        filtered_chars = [char.lower() for char in s if char.isalnum()]
        # isalnum() checks if the character is alphanumeric (letters and numbers) and filters out any other characters. 
        # The list comprehension creates a new list of lowercase alphanumeric characters from the original string.
        
        # Check if the filtered list of characters is the same forwards and backwards
        return filtered_chars == filtered_chars[::-1]   