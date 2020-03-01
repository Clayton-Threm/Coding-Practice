#Project Euler Question 29
#Distinct Powers

def power_set(x):
    power_list = set()
    for a in range(2,(x+1)):
        for b in range(2,(x+1)):
            power = (a**b)
            power_list.add(power)
    #print (power_list)
    return len(power_list)

print (power_set(100))