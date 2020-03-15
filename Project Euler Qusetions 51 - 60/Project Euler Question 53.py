#Project Euler Question 53
#Combinatoric selections


def factorial(x):
    if x > 1:
        return x * factorial(x - 1)
    else:
        return 1

comb_list = []
for x in range(1, 101):
    for y in range(1, 101):
        if y > x:
            break
        combinations = int(factorial(x) / (factorial(y) * factorial(x - y)))
        if combinations > 1000000:
            comb_list.append(x)

print (len(comb_list))