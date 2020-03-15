#Project Euler Question 55
#Lychrel numbers


def pal(x):
    num = str(x)
    if num == num[::-1]:
        return True
    else:
        return False

lychrel_list = []
for x in range(1, 10000):
    sum_x = x
    for y in range(1, 50):
        pal_x = str(sum_x)[::-1]
        sum_x += int(pal_x)
        if pal(sum_x) is True:
            break
    else:
        lychrel_list.append(x)
    #print (x, sum_x)

print (len(lychrel_list))