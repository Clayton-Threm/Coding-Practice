#Project Euler Question 23

#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
#For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

#A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
#By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
#However, this upper limit cannot be reduced any further by analysis,
#even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


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


def abundant_numbers_sum(num):
    non_abundant_sum_list = set()
    non_abundant_terms = set()
    abundant_sum = set()
    for num in range(1, (num+1)):
        non_abundant_sum_list.add(num)
        #print (num)
        for x, y in zip(range(1, ((int(num/2))+1)), range(num-1, int(num/2)-1, -1)):
            #print (x, y)
            counter = 0
            if x in non_abundant_terms:
                counter += 0
            elif x in abundant_sum:
                counter += 1
            elif sum(factor_finder(x)) > x:
                abundant_sum.add(x)
                counter += 1
            else:
                non_abundant_terms.add(x)

            if y in non_abundant_terms:
                counter += 0
            elif y in abundant_sum:
                counter += 1
            elif sum(factor_finder(y)) > y:
                abundant_sum.add(y)
                counter += 1
            else:
                non_abundant_terms.add(y)

            if counter == 2:
                non_abundant_sum_list.remove(num)
                break
                
    
    #print (non_abundant_sum_list)
    return sum(non_abundant_sum_list)

print (abundant_numbers_sum(28123))