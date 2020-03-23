#Project Euler Question 64
#Odd period square roots

import math
import decimal

decimal.getcontext().prec = 299
odd_count = 0
for num in range(1, 10000):
    repeat_list = []
    x = decimal.Decimal(num).sqrt()
    x1 = decimal.Decimal(math.modf(x)[1])
    y = x
    y1 = x1
    if math.modf(y)[0] == 0:
        continue
    while True:
        y = decimal.Decimal((y - y1)) ** decimal.Decimal(-1)
        y1 = decimal.Decimal(math.modf(y)[1])
        y_check = str(y)[:10]
        if (y_check in repeat_list):
            break
        else:
            repeat_list.append(y_check)
    if (len(repeat_list) % 2 != 0):
        odd_count += 1
    
print (odd_count)