#Project Euler Question 33
#Digit cancelling fractions

from fractions import Fraction
from functools import reduce

fraction_list = []
for a in range(10, 100):
	for b in range(10, 100):
		if b <= a:
			continue
		if str(a)[1] != str(b)[0]:
			continue
		if str(a)[0] >= str(b)[1]:
			continue
		if (a/b) != int(str(a)[0]) / int(str(b)[1]):
			continue
		frac = Fraction(a, b)
		fraction_list.append(frac)

fraction_total = reduce(lambda x, y: x*y, fraction_list)

#print (fraction_list)
print (fraction_total)