x = 1
while (x <= 20):
    y = ""
    F = "Fizz"
    B = "Buzz"
    if ((x % 3 == 0) or (x % 5 == 0)):
        if (x % 3 == 0):
            y += F
        if (x % 5 == 0):
            y += B
        print (y)
    else:
        print (x)
    x += 1
    
print("done")