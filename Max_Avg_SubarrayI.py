# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000


# Code:


from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # Step 1: Calculate the sum of the first 'k' elements
        current_sum = sum(nums[:k])
        
        # Step 2: Initialize the maximum sum as the sum of the first 'k' elements
        max_sum = current_sum
        
        # Step 3: Slide the window across the array
        for i in range(k, len(nums)):
            # Subtract the element that is left out of the window and add the new element
            current_sum = current_sum - nums[i - k] + nums[i]
            
            # Update the maximum sum if the current sum is greater
            max_sum = max(max_sum, current_sum)
        
        # Step 4: Return the maximum average
        return max_sum / k
