#Project Euler Question 26
#Reciprocal cycles

import math
def prime_finder(x):
    num = 3
    primes = [2]
    while (num < x):
        for prime in primes:
            if prime > (int(math.sqrt(num) + 1)):
                primes.append(num)
                break
            if num % prime == 0:
                break
        else:
            primes.append(num)
        num += 2
    return primes


def cycle_check(denominator):
    count = 1
    while denominator > 5:
        if (((10 ** count) - 1) % denominator == 0):
            return count

        count += 1
    return 0


def decimal_cycles(x):
    primes = prime_finder(x)
    longest = 0
    for num in primes:
        length = cycle_check(num)
        if length > longest:
            longest = length
            result = num
            #print (num, "is the denominator,", length, "is the cycle length")
    return result

print (decimal_cycles(1000), "has the longest repeating cycle")