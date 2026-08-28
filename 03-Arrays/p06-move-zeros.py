"""
Problem   : Move Zeroes (Easy)
Topic     : Arrays
Link      : https://leetcode.com/problems/move-zeroes/description/
Approach:
    Two-pointer approach:
    - Initialize k = 0 to track the position where the next non-zero
      element should be placed.
    - Traverse the array with i.
    - If nums[i] != 0:
        - swap nums[i] and nums[k]
        - increment k
    - All zeros naturally get pushed to the end, non-zero elements
      keep their relative order.
Time Complexity  : O(N)
Space Complexity : O(1)
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0

        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[i], nums[k] = nums[k], nums[i]

                k += 1
