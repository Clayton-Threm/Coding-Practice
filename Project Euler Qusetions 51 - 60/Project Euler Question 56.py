#Project Euler Question 56
#Powerful digit sum

highest_sum = 1
for a in range(1, 100):
    for b in range(1, 100):
        ab = (a ** b)
        digit_sum = sum(int(i) for i in str(ab))
        if digit_sum > highest_sum:
            highest_sum = digit_sum

print (highest_sum)