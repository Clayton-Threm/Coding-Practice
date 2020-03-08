#Project Euler Question 46
#Goldbach's other conjecture

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

def goldbach():
    prime_list = [2, 3]
    x = 3
    while True:
        x += 2
        Is_a_sum = False
        if x == prime_list[-1]:
            continue
        if prime_check(x) is True:
            prime_list.append(x)
            continue
        for prime in prime_list:
            square_num = 0
            while True:
                square_num += 1
                square = 2 * (square_num ** 2)
                if square > (x - prime):
                    break
                elif (square + prime) == x:
                    Is_a_sum = True
                    break
            if Is_a_sum is True:
                break
        else:
            return x

print (goldbach())