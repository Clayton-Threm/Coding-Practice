#Project Euler Question 39
#Integer right triangles

import math
import itertools
def right_triangle(x):
    triangle_list = []
    z1 = range(3, int(x/3)+1)
    z2 = range(int(x/4), int(x/2)+1)
    listy = [var for var in itertools.product(z1, z2) if (var[0] < var[1])]
    #print (listy)
    for a, b in listy:
        c = ((a**2 + b**2)**0.5)
        if ((c).is_integer()) and (a + b + c == x):
            triangle_set = [a, b, int(c)]
            #print (triangle_set, x)
            triangle_list.append(triangle_set)
    return triangle_list

def perimeter_triangle(x):
    highest = 0
    highest_list = []
    highest_per = 0
    for p in range(2, (x + 1), 2):
        tri_list = right_triangle(p)
        if len(tri_list) > highest:
            print (tri_list, p)
            highest = len(tri_list)
            highest_list = tri_list
            highest_per = p
    #print (highest_list, highest_per)
    return highest_per

print (perimeter_triangle(1000))