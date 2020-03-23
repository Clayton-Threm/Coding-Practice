#Project Euler Question 65
#Convergents of e

converge_list = [2, 3]
count = 2
multiple = 0
for x in range(3, 101):
    count += 1
    if count != 3:
        x = sum(converge_list[-2:])
        converge_list.append(x)
    else:
        count = 0
        multiple += 2
        x = (converge_list[-2] + (converge_list[-1] * multiple))
        converge_list.append(x)

print (sum(int(i) for i in str(converge_list[-1])))