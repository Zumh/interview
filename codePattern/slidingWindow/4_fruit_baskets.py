def fruits_into_baskets(fruits:list[str])->int:
    """
    Problem Statement #
Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the baskets.

Example 1:

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Time Complexity: O(n)
The step for searching sub array remain constant size n.

Space Complexity: O(1))
The memory space stay constant
    """
    baskets = {}
    basket_size = 2
    max_fruit = 0
    window_start = 0
    for index in range(len(fruits)):
        if fruits[index] not in baskets:
            baskets[fruits[index]] = 0
        baskets[fruits[index]] += 1

        while len(baskets) > basket_size:
            baskets[fruits[index]] -= 1
            if baskets[fruits[index]] == 0:
                del baskets[fruits[index]]

            window_start += 1
        max_fruit = max(max_fruit, index - window_start + 1)
    return max_fruit

fruits = ['A', 'B', 'C', 'A', 'C']
print(fruits_into_baskets(fruits))
