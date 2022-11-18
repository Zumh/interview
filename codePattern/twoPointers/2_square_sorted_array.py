def make_squares(nums:list[int])->list[int]:
    """
    Problem Statement #
    Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

    Example 1:

        Input: [-2, -1, 0, 2, 3]
        Output: [0, 1, 4, 4, 9]

    Time Complexity : O(n/2) -> O(n) 
    ignore constant

    Space Complexity : O(n)
    space grow as the input data size
    """

    sqr_list = [0]*len(nums)
    left = 0
    sqr_indx = right = len(nums) - 1
    while left <= right:

        left_sqr = nums[left] * nums[left]
        right_sqr = nums[right] * nums[right]
        
        if left_sqr > right_sqr:
            sqr_list[sqr_indx] = left_sqr
            left += 1
        else:
            sqr_list[sqr_indx] = right_sqr
            right -= 1

        sqr_indx -= 1
    return sqr_list

nums = [-2, -1, 1, 2,3]
print(make_squares(nums))
