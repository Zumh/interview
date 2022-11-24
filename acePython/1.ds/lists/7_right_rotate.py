
def right_rotate(nums:list[int], k:int)->list[int]:
    """
    Problem Statement#
Implement a function right_rotate(lst, k) which will rotate the given list by k. This means that the right-most elements will appear at the left-most position in the list and so on. You only have to rotate the list by one element at a time.

Input#
A list and a positive number by which to rotate that list

Output:#
The given list rotated by k elements

Sample Input#
lst = [10,20,30,40,50]
k = 3
What if the given input k is greater than the length of the lst?

Sample Output#
lst = [30,40,50,10,20]
    """
    nums_rotate = []

    if len(nums) == 0:
        k = 0
    else:
        # moding k with size of given list allow us get the right size from the start of a list
        k = k % len(nums)

    # get the k size of the right size from a list 
    # append that on the left size of a new list in same order 
    for indx in range(len(nums) - k, len(nums)):
        nums_rotate.append(nums[indx])

    # get the remaining left size of a given list and append with on a new list 
    for indx in range(0, len(nums)-k):
        nums_rotate.append(nums[indx])
    return nums_rotate
nums = [10,20,30,40,50]
k = 3
print(right_rotate(nums, k))

# more pythonic way to get it done 
def right_rotate_py(nums:list[int], k:int)->list[int]:
    """
    take right most elements from the list and append it on the left most.
    Take the remaining elements and append it.
    """

    # we still need to find the modulo of k % len(nums) times. 

    if len(nums) == 0:
        k = 0
    else:
        k = k % len(nums)

    return nums[len(nums)-k:] + nums[:len(nums)-k]

nums = [10,20,30,40,50]
k = 3
print(right_rotate_py(nums, k))

