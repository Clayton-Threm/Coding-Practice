#Project Euler Question 51
#Prime digit replacements

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

def multiple_prime_check(t, y):
    if prime_check(t) is False:
        return []
    number = str(t)
    number = [i for i in number]
    text = number.copy()
    numbers = [i for i in range(0, 10)]
    text_list = {}

    for x in numbers:
        x = str(x)
        c = text.count(x)
        if c > 0:
            index = [i for i in range(len(text)-1) if text[i] == (x)]
            text_list.update({x: index})

    #print ("".join(text), text_list)

    for digit, indexes in text_list.items():
        prime_list = []
        counter = 0
        if len(indexes) == 0:
            continue
        for x in numbers:
            for index in indexes:
                text[index] = str(x)
            int_text = (int("".join(text)))
            if (prime_check(int_text) is False) or (len(str(int_text)) < len(number)):
                counter += 1
                if counter > y:
                    break
            else:
                prime_list.append("".join(text))
        else:
            return prime_list
        text = number.copy()
    else:
        return []

def multiple_primes(y):    
    x = 11
    y = (10 - y)
    while True:
        x += 2
        check = multiple_prime_check(x, y)
        if len(check) > 0:
            return check[0]

print (multiple_primes(8))