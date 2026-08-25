"""
Problem   : Largest Element (Easy)
Topic     : Arrays
Link      : *not on LeetCode — from Striver's A2Z Sheet*

Approach:
    Traverse the array once, tracking the max seen so far — start with
    arr[0], update whenever a larger element is found.

Alternate (built-in):
    Python's max() does this in one line, but it's still O(N) under the
    hood — using it here would skip the point of practicing the traversal.

Time Complexity  : O(N)
Space Complexity : O(1)
"""

class Solution:
    def largest_element(self, nums: list[int]) -> int:
        return max(nums)

    def largest_element(self, nums: list[int]) -> int:
        largest = nums[0]
        
        for i in nums:
            if i > largest:
                largest = i
        return largest