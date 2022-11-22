
def find_first_unique(nums:list[int])->int:
    """
    Goal: Find first non repeat number from a given list
    Method: Brute force
    Description: brute force O(n^2) is the only way to find non repeat first number because of list data structure.
    We can more optimal way with hashmap data structure.
    """
    non_repeat_num = 0
    found = False
    for indx, num in enumerate(nums):
        inner_indx = indx 
        for inner_indx in range(indx+1, len(nums)):
            if num == nums[inner_indx]:
                found = True
                break
        if not found:
            non_repeat_num = num
            break 
    return non_repeat_num

nums = [9,2,3,2,6,6]
print(find_first_unique(nums))
nums = [4,5,1,2,0,4]
print(find_first_unique(nums))