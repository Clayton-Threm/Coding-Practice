#Project Euler Question 41
#Pandigital prime

import math
import itertools
def prime_check(x):
    if x > 2:
        if x % 2 == 0:
            return False
        else:
            for factor in range(3, int(math.sqrt(x) + 1), 2):
                if (x % factor) == 0:
                    return False
            else:
                return True
    elif x == 2:
        return True
    else:
        return False


def pan_check():    
    pan_range = [str(var) for var in range(1, 10)]
    for x in range(9, 0, -1):
        pan_list = [int("".join(var)) for var in itertools.permutations(pan_range[:x])]
        for perm in pan_list[::-1]:
            if prime_check(perm) is True:
                return perm

print (pan_check())