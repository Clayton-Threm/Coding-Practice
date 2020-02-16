#Project Euler Question 16

#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

#What is the sum of the digits of the number 2^1000?

x = 2**1000
x = list(str(x))
for term in x:
    intterm = int(term)
    x[x.index(term)] = intterm

sum_x = sum(x)

print(sum_x, "is the sum of the digits of the number 2^1000")