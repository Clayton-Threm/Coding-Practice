#Project Euler Question 27
#Quadratic primes

import math
def prime_check(x):
    if x <= 1:
        return False
    for factor in range(2, int(math.sqrt(x) + 1)):
        if (x % factor) == 0:
            return False
    return True

n = 0
biggest_streak = 0
streak_a = 0
streak_b = 0
qprime_list = []
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        while n >= 0:
            test = (n**2) + (a * n) + b
            if prime_check(abs(test)) is True:
                qprime_list.append(abs(test))
                n += 1
            else:
                if len(qprime_list) > biggest_streak:
                    biggest_streak = len(qprime_list)
                    streak_a = a
                    streak_b = b
                    #print (a, b, qprime_list)
                qprime_list.clear()
                break
        n = 0

print (streak_a * streak_b)