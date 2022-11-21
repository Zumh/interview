def is_leap(year:int)->bool:
    """
    Write a leap year logic that will verify if given year is a leap.
    If it is a leap return True else False
    """
    leap = False
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            leap = True
    return leap 

nums = [2000, 2400, 1800, 1900, 2100, 2200, 2300, 2500]

for num in nums:
    print(num, is_leap(num))