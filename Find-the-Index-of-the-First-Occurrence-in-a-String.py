# 28. Find the Index of the First Occurrence in a String (Easy) 

# Note: Marked easy on Leetcode but was thought as medium from discussion.

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack. 

# Example 1: 

# Input: haystack = "sadbutsad", needle = "sad" 
# Output: 0 
# Explanation: "sad" occurs at index 0 and 6. The first occurrence is at index 0, so we return 0. 

# Example 2: 

# Input: haystack = "leetcode", needle = "leeto" 
# Output: -1 
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

# Thinking Process:

# I had the correct idea, just some difficulty implementing the code for that solution.

# First we will make sure that the range is such that we know when the last subset begins and it ends perfectly so that we don’t make any incomplete subsets. 


# for i in range(len(haystack) - len(needle) + 1):


# Then we check if the subset we choose starting at i still i + len(needle) is equal to the value of needle.

      
# if haystack[i : i+len(needle)] == needle:


# Then we return 1 or -1 based on the result.


Code: 

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # makes sure we don't iterate through a substring that is shorter than needle
        for i in range(len(haystack) - len(needle) + 1):
            # check if any substring of haystack with the same length as needle is equal to needle
            if haystack[i : i+len(needle)] == needle:
                # if yes, we return the first index of that substring
                return i
        # if we exit the loop, return -1        
        return -1
