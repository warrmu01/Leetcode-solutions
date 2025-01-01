# 202. Happy Number (Easy)

# Write an algorithm to determine if a number n is happy. 
# A happy number is a number defined by the following process: 
# Starting with any positive integer, replace the number by the sum of the squares of its digits. 
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
# Those numbers for which this process ends in 1 are happy. 

# Return true if n is a happy number, and false if not. 

# Example 1: 

# Input: n = 19 
# Output: true 
# Explanation: 12 + 92 = 82 82 + 22 = 68 62 + 82 = 100 12 + 02 + 02 = 1 

# Example 2: 

# Input: n = 2 
# Output: false

# Thinking Process:

# Was not able to do it on my own. I learned one of the solutions on leetcode. That solution turns the string into a list to make keeping track easy. We do not use pointers here. We keep a separate list with all the old answers to keep track of any patterns. We just keep the loop going of the until we find 1 or a pattern.

# Code:

class Solution:
    def array_elements(self, x):
        numeric_elements = []
        
        while x >= 1:
            numeric_elements.append(x % 10)
            x //= 10

        return numeric_elements 

    def isHappy(self, n: int) -> bool:
        output = 0
        output_record = []
        elements = self.array_elements(n)

        while output != 1:
            output = 0
            
            for i in range(len(elements)):
                output += (elements[i] * elements[i])

            if output in output_record:
                return False
            
            output_record.append(output)

            elements = self.array_elements(output)

        return True      
