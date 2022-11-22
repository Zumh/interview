
def find_product(nums:list[int])->list[int]:
    """
    Time Complexity: O(n)
    Because we get the product of a value from left to right and in reverse.

    Space Complexity: O(n)
    We add the products to a list call product
    """
    # multiply from the left to the right
    # carrier for the left product
    left = 1
    product = []
    
    # multiply everything of the right from current number and append it to the product list
    for num in nums:
        product.append(left)
        left = left * num

    # carrier for the product
    right = 1
    # multiply everthing of the left from current number from product variable
    for indx in range(len(nums) - 1, -1, -1):
        product[indx] = product[indx] * right
        right = right * nums[indx]

       
    print(product)
nums = [1,2,3,4]

find_product(nums)
