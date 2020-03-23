#Project Euler Question 62
#Cubic permutations


def cubic_permutations(total):
    cube_list = {}
    for x in range(1, 10000):
        cube_x = "".join(sorted(str(x ** 3)))
        if cube_x in cube_list:
            cube_list[cube_x].append(x)
        else:
            cube_list[cube_x] = [x]
    for x, y in cube_list.items():
        if len(y) == total:
            result = (y[0] ** 3)
            return result

print (cubic_permutations(5))