"""
Problem   : Rotate Array (Medium)
Topic     : Arrays
Link      : https://leetcode.com/problems/rotate-array/description/
Approach:
    Reverse-thrice approach:
    - Normalize k with k %= len(nums), since k can be >= len(nums).
    - Reverse the entire array (0 to n-1).
    - Reverse the first k elements (0 to k-1).
    - Reverse the remaining elements (k to n-1).
    - This effectively rotates the array to the right by k steps in-place.
Time Complexity  : O(N)
Space Complexity : O(1)
"""

class Solution:
    def reverse(self, nums: list[int], start: int, end: int) -> list[int]:
        """
        THIS IS THE METHOD FOR REVERSING THE LIST
        """
        n = end - start + 1
        for i in range (n//2):
            nums[start + i], nums[end - i] = nums[end - i], nums[start + i]

        return nums

    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) == k:
            return

        elif len(nums) < k:
            k = k % len(nums)

            if k == 0:
                return

        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k -1)
        self.reverse(nums, k, len(nums)-1)
