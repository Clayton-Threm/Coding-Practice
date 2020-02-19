#Project Euler Question 18

#By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

#3
#7 4
#2 4 6
#8 5 9 3

#That is, 3 + 7 + 4 + 9 = 23.

#Find the maximum total from top to bottom of the triangle below:

grid = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

grid = grid.replace("00", "0")
grid = grid.replace("01", "1")
grid = grid.replace("02", "2")
grid = grid.replace("03", "3")
grid = grid.replace("04", "4")
grid = grid.replace("05", "5")
grid = grid.replace("06", "6")
grid = grid.replace("07", "7")
grid = grid.replace("08", "8")
grid = grid.replace("09", "9")

grid = [(row.split(" ")) for row in grid.split("\n")]
for row in grid:
    for term in row:
        intterm = int(term)
        row[row.index(term)] = intterm

y = 1
high_term = []

for row in grid[-1:-2:-1]:
    #print (row)
    for term in row:
        #print (term)
        #print (row[y])
        if term >= row[y]:
            high_term.append(term)
        else:
            high_term.append(row[y])
        y += 1
        if y >= len(row):
            break
    y = 1
y = 1
#print (high_term)

old_high_term = high_term.copy()
new_high_term = []
#new_high_list = []
z = 0

for row in grid[-2::-1]:
    #print (row, "is the current row")
    if len(new_high_term) == 1:
        highest_sum = new_high_term
        highest_sum.append(row[0])
        highest_sum = sum(highest_sum)
        break
    else:
        new_high_term.clear()
    for term in row:
        #print (term)
        check1 = (term + old_high_term[z])
        check2 = (row[y] + old_high_term[z+1])
        if check1 >= check2:
            new_high_term.append(check1)
        else:
            new_high_term.append(check2)
        y += 1
        z += 1
        if z >= (len(old_high_term)-1):
            break
    #print (new_high_term, "is the current list of high sums")
    old_high_term.clear()
    old_high_term = new_high_term.copy()
    y = 1
    z = 0

print (highest_sum, "is the highest sum")