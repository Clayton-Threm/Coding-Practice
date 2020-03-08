#Project Euler Question 45
#Triangular, pentagonal, and hexagonal


def pentagon_number(x, step):
    if x == 1:
        return 1
    else:
        n = step
        while True:
            n += 1
            penn = int(((3 * n) - 1) * n / 2)
            if penn > x:
                return [penn_save, n -1]
            elif penn == x:
                return [penn, n]
            else:
                penn_save = penn

def triangle_number(x, step):
    if x == 1:
        return 1
    else:
        n = step
        while True:
            n += 1
            trin = int((n + 1) * n / 2)
            if trin > x:
                return [trin_save, n - 1]
            elif trin == x:
                return [trin, n]
            else:
                trin_save = trin

x = 1
pen_step = 1
tri_step = 1
triple_list = [1]
while True:
    x += 1
    hex_x = x * ((2 * x) - 1)
    pent_x = pentagon_number(hex_x, pen_step)
    pen_step = pent_x[1]
    tri_x = triangle_number(hex_x, tri_step)
    tri_step = tri_x[1]
    if (hex_x == pent_x[0] == tri_x[0]):
        triple_list.append(hex_x)
    if len(triple_list) == 3:
        break

print (triple_list[2])