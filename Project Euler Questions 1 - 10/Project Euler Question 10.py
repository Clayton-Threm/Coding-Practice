#Project Euler Question 10

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

import math
def prime_sum(x):
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
    return sum(primes)


print (prime_sum(2000000), "is the sum")