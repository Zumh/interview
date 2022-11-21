
def find_sum(nums:list[int], k:int)->list[int]:
    """
        Time Complexity: O(nlogn) 
        Because we use built-in sort method and it takes O(nlogn) to sort the list
        Space Complexity: O(1) 
        Because we didn't create or use more than constant two number that sum up to k
    """
    left = 0
    right = len(nums) - 1
    nums.sort()

    while left < right:

        number_sum = nums[left] + nums[right]
        
        if number_sum == k:
            return [nums[left], nums[right]]
        elif number_sum > k:
            right -= 1
        elif number_sum < k:
            left += 1
    return []
nums = [1,21,3,14,5,60,7,6]
k = 81
print(find_sum(nums, k))

def find_sum_hash(nums:list[int], k:int)->list[int]:
    """
    Time Complexity: O(n) 
    we linearly search and find the second value that addds up to k
    Space Complexity: O(n)
    the key value pair space grows larger as the given data bigger
    the process or steps it takes to store the value in the extra space increase as the data increase
    """

    result = {}

    for indx, num in enumerate(nums):

        diff = k - num

        if diff not in result:
            result[num] = indx
        else:
            return [diff,num]
    return []
nums = [1,21,3,14,5,60,7,6]
k = 81
print(find_sum_hash(nums, k))


