#Project Euler Question 66
#Diophantine equation

import math
from decimal import *
getcontext().prec = 99

def is_integer(d):
    return d == d.to_integral_value()

def diophantine_equation(num):
    diophantine_list = {}
    for n in range(1, (num+ 1)):
        if is_integer(Decimal(math.sqrt(n))) is True:
            continue
        a = math.ceil(math.sqrt(n))
        a1 = a
        b = 1
        k = (a ** 2) - n
        if k == 1:
            diophantine_list[n] = a
        else:
            while True:
                m = a1
                m -= 1
                while True:
                    m += 1
                    m2 = (m ** 2)
                    saved_frac = Decimal(a + (b * m)) / Decimal(k)
                    if is_integer(saved_frac):
                        break
                a2 = Decimal((a * m) + (n * b)) / Decimal(math.fabs(k))
                b2 = Decimal(a + (b * m)) / Decimal(math.fabs(k))
                k2 = Decimal((m ** 2) - n) / Decimal(k)
                a = a2
                b = b2
                k = k2
                if k2 == 1:
                    diophantine_list[n] = int(a2)
                    break
    return (list(diophantine_list.keys())[list(diophantine_list.values()).index(max(diophantine_list.values()))])


print (diophantine_equation(1000))