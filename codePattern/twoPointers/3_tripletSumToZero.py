
def search_triplets(nums:list[int])->list[list[int]]:
    """
        Problem Statement #
        Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

        Example 1:

            Input: [-3, 0, 1, 2, -1, 1, -2]
            Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
            Explanation: There are four unique triplets whose sum is equal to zero.

            a + b + c = 0
            a + b = -c
            -(a+b) = c
    """

    triplet = [-1,-1]
    
    left = 0
    right = len(nums) - 1
    
    total_sum = 0
    
    found = False
    while left < right and not found:
        
        total_sum = nums[left] + nums[right]

        if total_sum == 0: 

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
