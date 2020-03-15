#Project Euler Question 57
#Square root convergents

fraction_list = 0
x = 3
y = 2
for num in range(1, 1000):
    xy = x + y
    x = xy + y
    y = xy
    if len(str(x)) > len(str(y)):
        fraction_list += 1

print (fraction_list)