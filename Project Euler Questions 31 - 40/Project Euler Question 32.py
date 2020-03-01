#Project Euler Question 32
#Pandigital Sums

pan_nums = set()
for a in range(100,5000):
    for b in range(2,100):
        if "0" in (str(a) or str(b)):
            continue
        if (len(str(a)) + len(str(b))) == 5:
            c = a * b
            if "0" in str(c):
                continue
            if (len(str(a)) + len(str(b)) + len(str(c))) == 9:
                pan_checker2 = []
                pan_checker = str(a) + str(b) + str(c)
                pan_checker2[:] = pan_checker
                pan_set = set(pan_checker2)
                if len(pan_set) == 9:
                    pan_nums.add(c)
                    #print (a, b, c)
                    #print (pan_set)

print (sum(pan_nums))