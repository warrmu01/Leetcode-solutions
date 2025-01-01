# 344. Reverse String (Easy) 

# Write a function that reverses a string. The input string is given as an array of characters s. 
# You must do this by modifying the input array in-place with O(1) extra memory. 

# Example 1: 

# Input: s = ["h","e","l","l","o"] 
# Output: ["o","l","l","e","h"] 

# Example 2: 

# Input: s = ["H","a","n","n","a","h"] 
# Output: ["h","a","n","n","a","H"]

# Thinking Process: 

# We use the concept of Two pointers with one pointer on each end and then just switch the values on each end one by one and keep moving the pointers toward the center of the list until the start is no longer less than the end.

# Note: make sure the pointers towards the end of the list (not the start) is -1 of the length of the list

# Code:

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        Start = 0
        End = len(s) - 1

        while Start < End:
            s[Start], s[End] = s[End], s[Start]
            Start += 1
            End -= 1
