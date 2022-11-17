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