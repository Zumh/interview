import math

def find_minimum(nums:list[int])->int:


    """
    find the minimum of a given list value
    Time Complexity: O(n)
    Traverse the data as the data increase

    Space Complexity: O(n)
    we don't need extra space
    """

    min_value = math.inf
    if len(nums) == 0:
        return None
    for num in nums:
        if min_value > num:
            min_value = num
    return min_value

nums = [9,2,3,6]

print(find_minimum(nums))
