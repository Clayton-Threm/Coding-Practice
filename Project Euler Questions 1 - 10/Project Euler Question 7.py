#Project Euler Question 7

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

import math
def prime_finder(x):
    num = 3
    primes = [2]
    while (x > 0):
        for prime in primes:
            if prime > (int(math.sqrt(num) + 1)):
                primes.append(num)
                if (len(primes) == x):
                    return ("{:,}".format(primes[-1]))
                break
            if num % prime == 0:
                break
        else:
            primes.append(num)
            if (len(primes) == x):
                break
        num += 2
    return ("{:,}".format(primes[-1]))


print (prime_finder(10001), "is the nth prime number")
