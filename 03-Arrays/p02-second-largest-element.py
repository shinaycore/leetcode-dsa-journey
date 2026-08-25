"""
Problem   : Second Largest Element (Easy)
Topic     : Arrays
Link      : *not on leetcode*

Approach:
    Traverse the array once, and keep a track of largest 
    and the second largest elements- update when largest
    element is found.

Edge Cases Considered:
    - if first element or num[0] is the largest, 
        hence we added an extra elif statement

Time Complexity  : O(N)
Space Complexity : O(1)
"""

class Solution:
    def second_largest_element(self, nums: list[int]) -> int:
        largest = float("-inf")
        second_largest = float("-inf")

        for num in nums:
            if num > largest:
                second_largest = largest
                largest = num
            
            elif num > second_largest and num != largest:
                second_largest = num
                
        return second_largest