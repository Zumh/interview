"""
Find the average of an array with K size. 
With brute force or using sliding window that is optimize.
"""

def find_average_array(nums:list[int], k:int)->list[int]:
    """
        This function use brute force technique for finding the average of each k size within array

    """


    averages = []
    
    innerIndex = 0
    outerIndex = 0
    numLength = len(nums)
    subLength = 0

    while outerIndex < numLength and subLength < numLength:
        subLength = outerIndex + k
        innerIndex = outerIndex
        sum = 0
        # sum up within the window 
        while innerIndex < subLength:
            sum += nums[innerIndex]
            innerIndex += 1
        averages.append(sum/k)
        outerIndex += 1 
    return averages
nums = [1,3,2,6,-1,4,1,8,2]
print(find_average_array(nums,5))

# Window sliding average sub array
def find_average_array_slide(nums:list, k:int)->list[int]:
    """
        Sliding window allow us to optimize the algorithm effeciency from O(N^2) to O(N)
    """
    averages = []

    totalSum = 0
    startWindow = 0
    endWindow = k 
    for current_index, num in enumerate(nums):
        
        # get a new total sum within the k size
        totalSum += num 

        endWindow = current_index

        # keep the window size within given k size.
        if endWindow+1 >= k:
            # calculate the average of subarray 
            averages.append(totalSum/k)

            # update a new total by removing the first value from the total sum
            totalSum = totalSum - nums[startWindow]

            # move the endWindow forward 
            endWindow += 1
            # move the startWindow forward
            startWindow += 1
         
    return averages 
nums = [1,3,2,6,-1,4,1,8,2]
print(find_average_array_slide(nums,5))

