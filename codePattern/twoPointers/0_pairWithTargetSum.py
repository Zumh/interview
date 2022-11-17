
def pair_with_targetsum(nums:list[int], target_sum:int)->list[int]:
    """
    Problem Statement #
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Example 1:

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
    """

    pair = [-1,-1]
    
    left = 0
    right = len(nums) - 1
    
    total_sum = 0
    
    found = False
    while left < right and not found:
        
        total_sum = nums[left] + nums[right]

        if total_sum == target_sum:

            pair = [left, right]
            found = True
        elif total_sum < target_sum:
            left += 1
        else:
            right -= 1

    return pair
nums = [1,2,3,4,6]
target_sum = 6

print(pair_with_targetsum(nums, target_sum))
