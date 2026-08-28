"""
Problem   : Single Number (Easy)
Topic     : Arrays / Bit Manipulation
Link      : https://leetcode.com/problems/single-number/
Approach:
    XOR approach:
    - Initialize result = 0.
    - Traverse the array, XOR-ing every element into result.
    - Since a ^ a = 0 and a ^ 0 = a, every number that appears twice
      cancels itself out, leaving only the number that appears once.
    - XOR is also commutative and associative, so the order of
      elements doesn't matter.
Time Complexity  : O(N)
Space Complexity : O(1)
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        result = 0

        for num in nums:
            result = result ^ num

        return result
