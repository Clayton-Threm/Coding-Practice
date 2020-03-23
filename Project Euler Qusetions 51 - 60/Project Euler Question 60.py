#Project Euler Question 60
#Prime pair sets

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


def prime_pair_sets():
    prime_set = [3, 7]
    x = 7
    while True:
        x += 2
        if prime_check(x) is False:
            continue
        for prime in prime_set:
            prime_test = str(prime) + str(x)
            if prime_check(int(prime_test)) is False:
                break
            prime_test = str(x) + str(prime)
            if prime_check(int(prime_test)) is False:
                break
        else:
            prime_set.append(x)
            if len(prime_set) == 5:
                return sum(prime_set)
        if x > 10000:
            x = prime_set[-1]
            prime_set.pop(-1)
            

print (prime_pair_sets())