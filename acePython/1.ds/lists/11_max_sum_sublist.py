
def find_max_sum_sublist(nums:list[int])->int:

    """
    Given an integer list, return the maximum sublist sum. The list may contain both positive and negative integers and is unsorted.
    we going to use kadane's dynamic programming 
    Sample input - [-4,2,-5,1,2,3,6,-5,1]
Sample output#
largest_sum = 12
    Time complexity: O(n)

    """

    current_max = 0
    global_max = 0

    for indx in range(0, len(nums)):

        # if current max is negative then get a new value from the list 
        if current_max < 0:
            current_max = nums[indx]
        else:
            # culculate urrent max sum 
            current_max += nums[indx]

        # keep updating the final max elements total sum
        if global_max < current_max:
            global_max  = current_max
    
    return global_max

nums = [-4,2,-5,1,2,3,6,-5,1]

print(find_max_sum_sublist(nums))