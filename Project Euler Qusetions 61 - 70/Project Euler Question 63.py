#Project Euler Question 63
#Powerful digit counts

same_len_list = 0
y = 0
while True:
    counter = 0
    y += 1
    for x in range(1, 10):
        power = (x ** y)
        if len(str(power)) == y:
            same_len_list += 1
            counter += 1
    if counter == 0:
        break

print (same_len_list)