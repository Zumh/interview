
def remove_even(nums:list[int])->list[int]:
    """
    remove even numbers from the given parameter lists
    Time Complexity: O(n)
    Linear search and appending only odd numbers
    Space Complexity: O(n)

    """
    result = []

    for indx, num in enumerate(nums):
        if num%2 != 0:
            result.append(num)
    # More pythonic way of doing it 
    # list comprehension can also be done
    result_lst = [num for num in nums if num % 2 != 0]

    return result_lst
nums = [1,2,4,5,10,6,3]
print(remove_even(nums))
    
