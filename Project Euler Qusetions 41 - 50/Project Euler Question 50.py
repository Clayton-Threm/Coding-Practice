#Project Euler Question 50
#Consecutive prime sum

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

def con_prime_sums(num):
    prime_list = [2, 3, 5]
    highest_length = 2
    highest_x = 5
    highest_sum = [2, 3]
    for x in range(7, num, 2):
        if prime_check(x) is True:
            prime_list.append(x)
            prime_index = -1
            check = True
            while check is True:
                prime_index += 1
                prime_inded_start = prime_index
                prime_sum = [prime_list[prime_index]]
                if int((x ** (2 / 3)) + 1) <= prime_sum[0]:
                    break
                while check is True:
                    prime_index += 1
                    prime_step = prime_list[prime_index]
                    if int((x ** (2 / 3)) + 1) <= prime_sum[0]:
                        break
                    prime_sum.append(prime_step)
                    if (len(prime_sum) < highest_length) or (sum(prime_sum) < x):
                        continue
                    if sum(prime_sum) > x:
                        if len(prime_sum) <= highest_length:
                            check = False
                        prime_index = prime_inded_start
                        break
                    elif sum(prime_sum) == x:
                        if len(prime_sum) >= highest_length:
                            highest_length = len(prime_sum)
                            highest_x = x
                            highest_sum = prime_sum
                        check = False
                        break
                    else:
                        pass
    return highest_x


print (con_prime_sums(1000000))