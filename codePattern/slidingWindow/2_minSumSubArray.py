import math
def min_sum_sub_array(nums:list, target_sum)->int:
    """
    Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

    Example 1:

    Input: [2, 1, 5, 2, 3, 2], S=7 
    Output: 2
    Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

    Time Complexity: O(n)
    The inner loop run only within a fixed size subarray
    Space Complexity: O(1)
    """

    min_len = math.inf

    total_sum = 0

    start_window = 0

    end_window = 0

    # shrink the the sum if the target_sum is greater 
    for index, num in enumerate(nums):

        total_sum += num 
        end_window = index 
        # shrink the window
        while total_sum >= target_sum:
            # update the minimum length of the window
            min_len = min(min_len, end_window - start_window + 1)
            total_sum = total_sum - nums[start_window]
            start_window += 1
    if min_len == math.inf:
        return 0
    return min_len 
# nums = [2, 1, 5, 2, 3, 2]

nums = [2,1,5,2,8]
s = 7

print(min_sum_sub_array(nums, s))