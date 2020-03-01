#Project Euler Question 34
#Digit factorials

import math

num_list = []
for x in range(3, ((math.factorial(9) * 6) + 2)):
    total = [math.factorial(int(digit)) for digit in str(x)]
    if sum(total) == x:
        #print (x)
        #print (total)
        num_list.append(x)

print (sum(num_list))