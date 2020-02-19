#Project Euler Question 21

#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
#The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

#Evaluate the sum of all the amicable numbers under 10000.

def factor_finder(num):
    if num == 1:
        return [0]
    factors = [1]
    factor = 2
    for factor in range(2, int((num/2)+1)):
        if (num % factor == 0) and (factor != num):
            factors.append(factor)
    #print (num, factors)
    return factors

def amicable_number(num):
    amicable_numbers = set()
    for x in range(2, (num+1)):
        a = x
        a_sum = sum(factor_finder(x))
        #print (a_sum, "a sum")
        b = a_sum
        if a != b:
            b_sum = sum(factor_finder(b))
            #print (b_sum, "b sum")
            if (a == b_sum) and (b == a_sum):
                amicable_numbers.add(a)
                amicable_numbers.add(b)
    #print (amicable_numbers)
    return sum(amicable_numbers)

print (amicable_number(10000), "is the sum of amicable numbers under n")