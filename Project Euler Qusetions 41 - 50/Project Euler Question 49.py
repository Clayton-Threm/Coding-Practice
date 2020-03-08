#Project Euler Question 49
#Prime permutations

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

def prime_permutations(num):
    triple_list = []
    for x in range(1000, num):
        if prime_check(x) is True:
            perm_list = [x]
            perm_prime = [int("".join(var)) for var in itertools.permutations(str(x))]
            for n in range(1, 3):
                perm_check = (x + (n * 3330))
                if (perm_check in perm_prime) and (prime_check(perm_check) is True):
                    perm_list.append(perm_check)
            else:
                if len(perm_list) == 3:
                    triple_list.append(perm_list)
    else:
        result = [str(var) for var in triple_list[1]]
        return int("".join(result))

print (prime_permutations(10000))