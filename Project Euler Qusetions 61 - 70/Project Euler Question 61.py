#Project Euler Question 61
#Cyclical figurate numbers


def octagonal(n):
    return (n * ((3 * n) - 2))
def heptagonal(n):
    return int(n * ((5 * n) - 3) / 2)
def hexagonal(n):
    return (n * ((2 * n) - 1))
def pentagonal(n):
    return int(n * ((3 * n) - 1) / 2)
def sqaure(n):
    return (n ** 2)
def triangle(n):
    return int(n * (n + 1) / 2)

oct_list = []
hept_list = []
hex_list = []
pent_list = []
squ_list = []
tri_list = []
n = 0
while True:
    n += 1
    oct_x = octagonal(n)
    hept_x = heptagonal(n)
    hex_x = hexagonal(n)
    pent_x = pentagonal(n)
    squ_x = sqaure(n)
    tri_x = triangle(n)
    if 10000 > oct_x >= 1000:
        oct_list.append(oct_x)
    if 10000 > hept_x >= 1000:
        hept_list.append(hept_x)
    if 10000 > hex_x >= 1000:
        hex_list.append(hex_x)
    if 10000 > pent_x >= 1000:
        pent_list.append(pent_x)
    if 10000 > squ_x >= 1000:
        squ_list.append(squ_x)
    if 10000 > tri_x >= 1000:
        tri_list.append(tri_x)
    elif oct_x >= 10000:
        break

all_list = [hept_list, hex_list, pent_list, squ_list, tri_list]

def cycle_numbers():
    index_dict = {0: True, 1: True, 2: True, 3: True, 4: True}
    for oct_number in oct_list:
        cycle_list = {oct_number: 5}
        cycle_list_keys = list(cycle_list.keys())
        ignore_list = []
        check = int(str(oct_number)[2:])
        og_check = int(str(oct_number)[0:2])
        index = -1
        counter = 0
        while True:
            index += 1
            if index > 4:
                index = 0
            if index_dict[index] == False:
                continue
            for num in all_list[index]:
                if num in ignore_list:
                    continue
                if num in list(cycle_list.keys()):
                        continue
                check_2 = int(str(num)[0:2])
                if check_2 == check:
                    counter = 0
                    new_term = num
                    cycle_list[new_term] = index
                    cycle_list_keys = list(cycle_list.keys())
                    check = int(str(num)[2:])
                    index_dict[index] = False
                    if len(cycle_list) == 6:
                        if og_check == check:
                            return sum(cycle_list_keys)
                        else:
                            ignore_list.append(cycle_list_keys[-1])
                            index_dict[index] = True
                            del cycle_list[cycle_list_keys[-1]]
                            cycle_list_keys = list(cycle_list.keys())
                    break
            else:
                counter += 1
                if counter == 5:
                    counter = 0
                    ignore_list.append(cycle_list_keys[-1])
                    index_dict[cycle_list.get(cycle_list_keys[-1])] = True
                    cycle_list.popitem()
                    if len(cycle_list) == 0:
                        break
                    cycle_list_keys = list(cycle_list.keys())
                    check = int(str(cycle_list_keys[-1])[2:])

print (cycle_numbers())