#Project Euler Question 9

#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

def abc_finder(x):
    a = 1
    b = 2
    c = 3
    add = 0
    product = 0
    for c in range(3, x):
        for b in range(2, x):
            if (b > c):
                break
            for a in range(1, x):
                if a > (b or c):
                    break
                if (c**2 == (a**2 + b**2)):
                    add = (a + b + c)
                    #print (add, "is the add")
                    if (add == x):
                        triplet = [a, b, c]
                        product = (a * b * c)
                        #print ()
                        print (triplet, "is the pythagorean triplet")
                        product = ("{:,}".format(product))
                        return product


print(abc_finder(1000), "is the product for the pythagorean triplet")