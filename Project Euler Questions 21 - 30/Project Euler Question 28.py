#Project Euler Question 28
#Number Spiral Diagonals


def spiral_numbers(r):
    spiral_list = []
    count = -1
    gap = 2
    x = 1
    while x <= (r**2):
        spiral_list.append(x)
        count += 1
        if count == 4:
            gap += 2
            count = 0
        x += gap
    #print (spiral_list)
    return sum(spiral_list)

print (spiral_numbers(1001), "is the sum of the diagonals")