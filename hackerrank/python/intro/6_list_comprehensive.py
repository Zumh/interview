
def find_target_sum(x:int, y:int, z:int, target_sum:int)->list[int]:
    result = []

    # permutate the variables 
    permuate = [[x_1,y_1,z_1] for x_1 in range(x+1) for y_1 in range(y+1) for z_1 in range(z+1)]
    # find group of list that are not the same as target_sum
    print(permuate)

    # return the list

find_target_sum(2,3,5,6)