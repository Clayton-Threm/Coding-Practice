#Project Euler Question 36
#Double-base palindromes

def pal(x):
    num = str(x)
    if num == num[::-1]:
        return True
    else:
        return False

def check(num):
    double_base_list = set()
    for x in range(1, (num + 1)):
        if pal(x) is True:
            #print (x)
            base2 = (bin(x))[2:]
            if pal(base2) is True:
                #print (x, "in base 2 is", base2)
                double_base_list.add(x)
    #print (double_base_list)
    return sum(double_base_list)

print (check(1000000))