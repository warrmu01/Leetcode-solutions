# 125. Valid Palindrome (Easy) 

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers. 

# Given a string s, return true if it is a palindrome, or false otherwise. 

# Example 1: 
# Input: s = "A man, a plan, a canal: Panama" 
# Output: true 
# Explanation: "amanaplanacanalpanama" is a palindrome. 

# Example 2: 
# Input: s = "race a car" 
# Output: false 
# Explanation: "raceacar" is not a palindrome. 

# Example 3: 
# Input: s = " " 
# Output: true 
# Explanation: s is an empty string "" after removing non-alphanumeric characters. Since an empty string reads the same forward and backward, it is a palindrome.

# Thinking Process:

# I had the correct idea, just some issue with removing the spaces and making the input string all lowercase.  Other than that It was just the simple case of Two pointers on each end and checking if the values are the same or not.

# Loop example:

#     while Start < End:
#            		s[Start], s[End] = s[End], s[Start]
#            		Start += 1
#            		End -= 1

# Pointer Example:

# Start = 0
# End = len(s) - 1

# Code:


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove non-alphanumeric characters and convert to lowercase
        s = ''.join(c.lower() for c in s if c.isalnum())
        Start = 0
        End = len(s) - 1

        # Compare characters from both ends
        while Start < End:
            if s[Start] != s[End]:  # If mismatch found
                return False
            Start += 1  # Move Start pointer forward
            End -= 1    # Move End pointer backward

        return True  # Return True if no mismatch found
      


