"""
Problem   : Remove Duplicates from Sorted Array (Easy)
Topic     : Arrays
Link      : https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

Approach:
    Two-pointer approach:
    - Initialize i = 0 and j = 1.
    - j traverses the array.
    - i tracks the position of the last unique element.
    - If nums[i] != nums[j]:
        - increment i
        - copy nums[j] to nums[i]
    - Return i + 1.

Time Complexity  : O(N)
Space Complexity : O(1)
"""
class Solution:
    # this gives no. of duplicates inside the array and also removes the no. of duplicates
    # it takes extra space tho of worst case as O(N) where all elements are unique
    def removeDuplicates(self, nums: List[int]) -> int:
        list_size = len(nums)
        nums = list(set(nums))
        diff_in_size = list_size - len(nums)

        return diff_in_size

    # The two pointer approach
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums:
            return 0

        i = 0

        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i+1
