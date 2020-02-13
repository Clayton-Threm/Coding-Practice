#Project Euler Question 4

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.


def pal(n):
    number = str(n)
    return number == number[::-1]

def func_pal(x,y):
    bp = 0
    xs = x
    ys = y
    yh = 0
    result = 0
    while ((x and y) >= 1):
        result = (x * y)
        if (result >= bp):
            if pal(result):
                bp = result
                yh = y
                #print (x, "and", y, "are factors")
                #print (result, "is a palidrome")
                #print ()
                if (yh == ys):
                    break
        if (y > yh):
        	y -= 1
        else:
        	x -= 1
        	y = ys
    return bp


print(func_pal(999,999), "is the biggest palidrome")