#Project Euler Question 40
#Champernowne's constant

import functools
x = 0
cham = [0]
while True:
    x += 1
    cham.extend([int(var) for var in str(x)])
    if len(cham) > 1000000:
        break

#print (cham)
print (cham[1] * cham[10] * cham[100] * cham[1000] * cham[10000] * cham[100000] * cham[1000000])