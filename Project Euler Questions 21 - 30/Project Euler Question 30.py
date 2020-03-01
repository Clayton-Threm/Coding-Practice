#Project Euler Question 30
#Digit Fifth Powers


def power_sum_list(x):
    power_list = []
    for num in range(2, (10**(x+1))):
        digit_sum = sum(list([(int(digit)**x) for digit in str(num)]))
        if digit_sum == num:
            power_list.append(num)
    #print (power_list)
    return sum(power_list)

print (power_sum_list(5))