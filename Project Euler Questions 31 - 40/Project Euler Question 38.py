#Project Euler Question 38
#Pandigital multiples

def num_check(x):
    if "0" in str(x):
        return False
    for digit in range(1, 10):
        if str(x).count(str(digit)) > 1:
            return False
    else:
        return True

def uniqued(x):
    if "0" in str(check):
        return False
    for digit in range(1, 10):
        if str(check).count(str(digit)) > 1:
            return False
    if any(digit in str(check) for digit in str(strx)):
        return False
    if len(strx) > 9:
        return False
    else:
        return True


highest = 0
for x in range(1, 10000):
    unique = True
    mul = 1
    strx = [digit for digit in str(x)]
    if num_check(x) is False:
        continue
    while (len(strx) < 9) and (unique == True):
        mul += 1
        check = x * mul
        if uniqued(check) is False:
            unique = False
            break
        strx.extend(str(check))
    if unique == False:
        continue
    setx = {digit for digit in strx}
    if len(setx) == 9:
        #print (strx)
        strx = "".join(strx)
        strx = int(strx)
        #print (strx)
        if strx > highest:
            highest = strx

print (highest)