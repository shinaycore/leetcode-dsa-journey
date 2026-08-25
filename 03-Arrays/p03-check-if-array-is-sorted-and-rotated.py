"""
Problem   : Check if Array Is Sorted and Rotated (Easy)
Topic     : Arrays
Link      : https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/

Approach:
    Traverse the array once, check for the drops in the array,
    and if the drop is greater than 1, array is not sorted.

    for e.g.
    arr = [3, 4, 5, 1, 2] -> this is a sorted array and no of drop is 1 (from 5 to 1)
    arr = [3, 4, 5, 1, 2, 1] -> this is a sorted array and no of drops are 2 (from 5 to 1 and from 2 to 1)


Time Complexity  : O(N)
Space Complexity : O(1)
"""

class Solution:
    def check(self, nums: List[int]) -> bool:

        count = 0
        size = len(nums)

        for i in range(size):
            if(nums[i] > nums[(i+1) % size]):
                count += 1

        return count <= 1
