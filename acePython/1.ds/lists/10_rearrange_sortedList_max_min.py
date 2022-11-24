
def max_min(nums:list[int])->list[int]:
    """
        Problem Statement#
Implement a function called max_min(lst) which will re-arrange the elements of a sorted list such that the 0th index will have the largest number, the 1st index will have the smallest, and the 2nd index will have second-largest, and so on. In other words, all the even-numbered indices will have the largest numbers in the list in descending order and the odd-numbered indices will have the smallest numbers in ascending order.

Input:#
A sorted list

Output:#
A list with elements stored in max/min form

Sample Input#
lst = [1,2,3,4,5]
Sample Output#
lst = [5,1,4,2,3]
    """

    # manual way of max and min sorting
    # O(n) 
    max_min_result = []
    left = 0
    right = len(nums) - 1
    while left <= right:
        max_min_result.append(nums[right])
        max_min_result.append(nums[left])
        right -= 1
        left += 1
    return max_min_result
nums = [1,2,3,4,5,6,7]
nums = [1,2,3,4,5,6]
print(max_min(nums))

def max_min_mod(nums:list[int])->list[int]:
    """
        Problem Statement#
Implement a function called max_min(lst) which will re-arrange the elements of a sorted list such that the 0th index will have the largest number, the 1st index will have the smallest, and the 2nd index will have second-largest, and so on. In other words, all the even-numbered indices will have the largest numbers in the list in descending order and the odd-numbered indices will have the smallest numbers in ascending order.

Input:#
A sorted list

Output:#
A list with elements stored in max/min form

Sample Input#
lst = [1,2,3,4,5]
Sample Output#
lst = [5,1,4,2,3]
    """

    max_element = nums[-1] + 1
    min_element = nums[0]

    max_indx = len(nums) - 1
    min_indx = 0

    for indx, num in enumerate(nums):
        # store max value in even position
        if indx % 2 == 0:
            nums[indx] += (nums[max_indx] % max_element) * max_element
            max_indx -= 1
        # sotre min value in odd position 
        else:

            nums[indx] += (nums[min_indx] % max_element) * max_element
            min_indx += 1
    
    # extract numbers we store in the list 
    for indx, num in enumerate(nums):
        nums[indx] = num // max_element
    return nums
nums = [1,2,3,4,5,6,7]
print(max_min_mod(nums))
nums = [1,2,3,4,5,6]
print(max_min_mod(nums))