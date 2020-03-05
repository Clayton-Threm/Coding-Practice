#Project Euler Question 35
#Circular primes

import math
def prime_check(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    else:
        for factor in range(3, int(math.sqrt(x) + 1), 2):
            if (x % factor) == 0:
                return False
        else:
            return True


def circular_prime(x):
    cprime_list = {2, 3, 5, 7}
    ignore_digit = {"5", "2", "4", "6", "8"}
    for num in range(11, x, 2):
        if any(digit in ignore_digit for digit in str(num)):
            continue
        elif num in cprime_list:
            continue
        else:
            pass
        #print (num)
        if prime_check(num) is True:
            prime_check_list = {num}
            c_check = [i for i in str(num)]
            for digit in range(1, len(c_check)):
                c = c_check[-1]
                c_check.pop()
                c_check.insert(0, c)
                c_check = int("".join(c_check))
                if prime_check(c_check) is True:
                    #print (c_check)
                    prime_check_list.add(c_check)
                    c_check = [i for i in str(c_check)]
                else:
                    break
            else:
                cprime_list.update(prime_check_list)
                #print (num, prime_check_list)
    #print (cprime_list)
    return len(cprime_list)

print (circular_prime(1000000))