"""
Problem   : Max Consecutive Ones (Easy)
Topic     : Arrays
Link      : https://leetcode.com/problems/max-consecutive-ones/description/
Approach:
    Single-pass counter approach:
    - Initialize count = 0 to track the length of the current run of 1s.
    - Traverse the array.
    - If num == 1:
        - increment count
        - update output = max(output, count)
    - Else (num == 0):
        - reset count = 0, since the run is broken.
    - Return output.
Time Complexity  : O(N)
Space Complexity : O(1)

Brute Force (commented above):
    - For each index i, walk forward while nums[j] == 1, counting the run.
    - Track the max count seen.
    - Time Complexity  : O(N^2) worst case (e.g. all 1s), since every
      starting index re-walks the remaining run.
    - Space Complexity : O(1)
"""
class Solution:
    # # Brute Force
    # def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

    #     max_ones = 0
    #     j = 0

    #     for i in range (0, len(nums)):
    #         count = 0
    #         j = i
    #         while j < len(nums) and nums[j] == 1:
    #             j += 1
    #             count += 1

    #         max_ones = max(count, max_ones)

    #     return max_ones

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        output = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1

                output = max(output, count)

            else:
                count = 0

        return output
