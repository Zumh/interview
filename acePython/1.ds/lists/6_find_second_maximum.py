import math 
def find_second_maximum(nums:list[int])->int:
    """
    Gaol: find the second min value from a given list
    Methods: 
    1. sort the list with built-in, extract the second last max value from a list.  O(nlogn) because we use merge sort
    2. use two for loop to find the second max and the T is O(n).
    3. use one for loop and keep switching the second max with final max. T is O(n)

    We going to use method #3 because it require a simple for loop with same result as other methods.
    """
    second_max = last_max = - math.inf
    for indx, num in enumerate(nums):

        # if the last_max is less than current num then update the second_max and last_max 
        if num > last_max:
            second_max = last_max
            last_max = num 
        
        elif num > second_max and num != last_max:
        # update second_max if current num is greater and not the same as last_max
            second_max = num 

    if second_max == -math.inf:
        return 
        
    return second_max
nums=[9,2,3,6]
print(find_second_maximum(nums))
nums=[4,2,1,5,0]
print(find_second_maximum(nums))