#Project Euler, Question 3:

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?


def func_pf(x):
    factor = 2
    for var in range(0, x):
        if (x != 1):
            if (x % factor != 0):
                factor += 1
            else:
                x = (x / factor)
                print (factor, "is a prime factor,")
        else:
            print ()
            return factor
            #break
			#This break is useless, return will end it
            
print(func_pf(600851475143), "is the highest prime factor")