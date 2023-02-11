
def merge_lists(list1:list[int], list2:list[int])->list[int]:

    # merge two sorted lists assuming both have same length
    # we going to merge them in the first list
    # Time Complexity: O(m^2) if m > n otherise O(n^2)
    # extra space is not used but extends which left with O(m)
    result = []
    left = 0
    right = 0
    
    while left < len(list1) and right < len(list2):

        if list1[left] > list2[right]:
            list1.insert(left, list2[right])
            left += 1
            right += 1
        else:
            left += 1
    # get the last remain numbers
    if right < len(list2):
        list1.extend(list2[right:])
    return list1

num_1 = [1,3,4,5]
num_2 = [2,6,7,8]

print(merge_lists(num_1, num_2))
