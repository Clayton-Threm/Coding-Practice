#Project Euler Question 52
#Permuted multiples

def same_digits(x, y):
    ld = x
    nld = y
    for digit in nld:
        if digit in ld:
            ld.remove(digit)
        else:
            return False
    else:
        return True

def multiples(num):
    x = 9
    while True:
        x += 1
        m = x
        str_x = str(x)
        list_of_digits = [digit for digit in str_x]
        for add in range(2, (num + 1)):
            m += x
            str_m = str(m)
            if len(str_m) > len(str_x):
                break
            new_list_of_digits = [digit for digit in str_m]
            if same_digits(new_list_of_digits, list_of_digits) is False:
                break
            #print (x, add, m)
        else:
            return x

print (multiples(6))