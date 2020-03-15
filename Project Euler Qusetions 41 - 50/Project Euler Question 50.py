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
    highest_sum = [2, 3]
    for x in range(7, num, 2):
        if prime_check(x) is False:
            continue
        prime_list.append(x)

    highest_x = 5
    highest_length = 2
    for start_index, prime in enumerate(prime_list):
        prime_sum = prime
        prime_save = prime_sum
        index_save = start_index
        sum_test = sum(prime_list[start_index:(highest_length + start_index - 1)])
        if sum_test > num:
            break
        for index, prime in enumerate(prime_list[(start_index + 1):], 1):
            prime_sum += prime
            if prime_sum >= num:
                index_length = (index_save + 1)
                if index_length >= highest_length:
                    highest_length = index_length
                    highest_x = prime_save
                    #print (highest_x, [prime_list[start_index], prime_list[index_save + start_index]], highest_length)
                break
            else:
                if prime_sum < highest_x:
                    continue
                if prime_sum in prime_list:
                    prime_save = prime_sum
                    index_save = index
    return highest_x


print (con_prime_sums(1000000))