
def even_odd(num:int):
    """
    Print Weird if the number is weird. Other wise, print Not Weird.
    Constraints
     1 <= n <= 1000
    Input Format 
    n > 0
    """

    number = num % 2

    if number != 0:
        message = "Weird"
    else:
        if 2 <= number <= 5:
            message = "Not Weird"
        elif 6 <= number <= 20:
            message = "Weird"
        
    print(message)

num = 3
even_odd(num)