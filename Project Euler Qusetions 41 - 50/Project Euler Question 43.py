#Project Euler Question 43
#Sub-string divisibility

import itertools
def pan_check():    
    pan_range = [str(var) for var in range(0, 10)]
    pan_list = [int("".join(var)) for var in itertools.permutations(pan_range)]
    divide_check = [2, 3, 5, 7, 11, 13, 17]
    pan_results = []
    for perm in pan_list:
        if len(str(perm)) != 10:
                continue
        divide_index = -1
        for x in range(7, 0, -1):
            perm_chunk = int(str(perm)[(x):(x+3)])
            if perm_chunk % divide_check[divide_index] != 0:
                break
            divide_index -= 1
        else:
            pan_results.append(perm)
    return sum(pan_results)


print (pan_check())