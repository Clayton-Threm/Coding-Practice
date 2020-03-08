#Project Euler Question 47
#Distinct primes factors


def prime_factorization(x, prime_list):
    pf_list = set()
    prime_index = 0
    check = x
    for var in range(0, check):
        if (check != 1):
            factor = prime_list[prime_index]
            if (check % factor != 0): 
                if factor > ((x / 2) + 1):
                    return "prime"
                prime_index += 1
            else:
                check = (check / factor)
                pf_list.add(factor)
        else:
            return pf_list

def distinct_factors(length):
    number_list = []
    prime_list = [2, 3, 5]
    x = 5
    while True:
        x += 1
        factor_list = prime_factorization(x, prime_list)
        if factor_list == "prime":
            prime_list.append(x)
            number_list.clear()
        elif len(factor_list) == length:
            number_list.append(x)
        else:
            number_list.clear()
        if len(number_list) == length:
            return number_list
            
print(distinct_factors(4))