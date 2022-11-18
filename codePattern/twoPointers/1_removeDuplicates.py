
def remove_duplicates(nums:list[int])->int:
    """
        Problem Statement #
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.

Example 1:

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
    """
    # we start our unique number by offsetting it to 1 
    next_unique_pos = 1
    curr_indx = 0

    # we also start from second position because we assume that first position 0 is a unique number itself
    for curr_indx, curr_num in enumerate(nums):
        

        # get the number just behind current number from array
        next_unique_num = nums[next_unique_pos - 1]

        # update or get a new unique num if we find a new unique number in  current number
        if next_unique_num != curr_num:
            nums[next_unique_pos] = curr_num

            # point to the next position in array for furthur update
            next_unique_pos += 1


    # get the distinct character len
    distinct_len = next_unique_pos

    return distinct_len

nums = [2,3,3,3,6,9,9]
print(remove_duplicates(nums))

def remove_duplicates_key(nums:list[int], key:int)->int:
    distinct_len = 0
    
    next_unique_pos = 0
    curr_indx = 0

    for curr_indx, curr_num in enumerate(nums):

        # if we found a new number different from input key, update unique values
        if curr_num != key:
            nums[next_unique_pos] = curr_num

            next_unique_pos += 1

    distinct_len = next_unique_pos
    return distinct_len
nums = [2,3,3,3,6,9,9]
key = 3 
print(remove_duplicates_key(nums, key))
