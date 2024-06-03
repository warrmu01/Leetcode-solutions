# GCD of Strings Problem
# In the context of the GCD of strings problem, the goal is to find the largest string X such that both 
# str1 and str2 can be constructed by concatenating X multiple times.

# For instance, the GCD of "ABCABC" and "ABC" is "ABC".

# Solution to GCD of Strings Problem:

# 1. Here's how you might implement the gcdOfStrings function:

# 2. Check if the concatenation of str1 and str2 in both orders is the same. If not, there is no common divisor.

# 3. Use the Euclidean algorithm to find the GCD of the lengths of str1 and str2.

# 4. The GCD string will be the prefix of either string up to the length of the GCD of their lengths.


# if you don't want to use gcd function from math lib use this:

class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # If concatenating str1 and str2 or str2 and str1 doesn't produce the same result, 
        # it means there's no common divisor, so you return an empty string.
        
        if str1 + str2 != str2 + str1:
            return ""

        # If str1 and str2 are of equal length, you return one of them (they're both divisors of each other).

        if len(str1) == len(str2):
            return str1

        # If one string is longer than the other, you recursively call the
        #  function with the longer string truncated by the length of the shorter one.
        
        if len(str1) > len(str2):
          return self.gcdOfStrings(str1[len(str2):], str2)
        return self.gcdOfStrings(str1, str2[len(str1):])


# Solution with gcd function:

class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # Check if concatenated strings are equal or not, if not return ""

        if str1 + str2 != str2 + str1:
            
            return ""
        
        # If strings are equal than return the substring from 0 to gcd of size(str1), size(str2)

        from math import gcd

        return str1[:gcd(len(str1), len(str2))]



