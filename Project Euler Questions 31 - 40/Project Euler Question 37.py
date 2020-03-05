#Project Euler Question 37
#Truncatable primes

import math
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

def trunc_check(num):
    x = 9
    bad_start = {"1", "9"}
    bad_end = {"1", "5", "9"}
    trunc_set = set()
    while True:
        x += 2
        if any(digit in bad_start for digit in str(x)[0]):
            continue
        if any(digit in bad_end for digit in str(x)[-1]):
            continue
        if prime_check(x) is True:
            #print (x)
            for digit in range(1, len(str(x))):
                if prime_check(int(str(x)[digit:])) is False:
                    break
                if prime_check(int(str(x)[:-digit])) is False:
                    break
            else:
                #print (x)
                trunc_set.add(x)
        if len(trunc_set) == num:
            break
    #print (trunc_set)
    return sum(trunc_set)

print (trunc_check(11))