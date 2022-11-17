
def max_sum_sub_array(nums:list[int], k:int)->int:
    """
    Time Complexity: O(n)
    Steps to find the max increase as data grow
    
    Space Complexity: O(1)
    We don't need extra container or space 

    """ 
    maxSum = 0
    totalSum = 0

    startWindow = 0
    endWindow = 0

    for index, num in enumerate(nums):

        totalSum += num 
        endWindow = index 

        if endWindow+1 >= k:

            # find the max 
            maxSum = max(maxSum, totalSum)
            
            totalSum = totalSum - nums[startWindow]

            # update the start window 
            startWindow += 1

    return maxSum    
nums = [2,1,5,1,3,2]
k = 3
print(max_sum_sub_array(nums, k))