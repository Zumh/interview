def square_numbers(max_num:int):
    """
    Square number that are < num print them
    """
    for num in range(max_num):
        print(num * num)
num = 3
square_numbers(num)