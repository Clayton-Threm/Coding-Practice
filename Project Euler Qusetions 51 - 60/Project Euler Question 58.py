#Project Euler Question 58
#Spiral primes

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

def spiral_numbers():
    spiral_list = set()
    prime_list = set()
    count = -1
    gap = 2
    x = 1
    side_length = 1
    while True:
        spiral_list.add(x)
        if prime_check(x) is True:
            prime_list.add(x)
        count += 1
        if count == 4:
            gap += 2
            side_length += 2
            count = 0
            percent = (len(prime_list) / len(spiral_list))
            if percent < 0.1:
                return side_length
        x += gap

print (spiral_numbers())