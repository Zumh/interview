
def rearrange(nums:list[int])->list[int]:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    results = [0] * len(nums)
    left = 0
    right = len(nums) - 1

    for indx, num in enumerate(nums):
        
        if nums[indx] >= 0:
            results[right] = num
            right -= 1
        else:
            results[left] = num
            left += 1
 
        
    return results
nums = [10,-1,20,4,5,-9,-6]
print(rearrange(nums))

def rearrange_twop(nums:list[int])->list[int]:
    """
    Better algorithm because we eliminate the space problem from above algorithm.
    Using two pointer technique we can rearrange positive and negative values.
    If right is negative then switch left value with the right value.
    Time Complexity: O(n)
    Space Complexity: O(1)

    """
    left = 0
    right = 0

    for right in range(len(nums)):

        if nums[right] < 0:
            nums[right], nums[left] = nums[left], nums[right]
            left += 1
    return nums 
nums = [10,-1,20,4,5,-9,-6]
print(rearrange_twop(nums))


def rearrange_pythonic(nums:list[int])->list[int]:
    return[left_num for left_num in nums if left_num < 0] + [right_num for right_num in nums if right_num >= 0]
nums = [10,-1,20,4,5,-9,-6]
print(rearrange_pythonic(nums))

