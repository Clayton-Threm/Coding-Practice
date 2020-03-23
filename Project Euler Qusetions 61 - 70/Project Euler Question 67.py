#Project Euler Question 67
#Maximum path sum II


with open("C:\\Users\\Clayton\\Documents\\Python Other Files\\p067_triangle.txt") as tri_file:
    content = tri_file.read()

grid = content
grid = [(row.split(" ")) for row in grid.split("\n")]
grid.pop(-1)
for row in grid:
    for term in row:
        intterm = int(term)
        row[row.index(term)] = intterm

y = 1
high_term = []

for row in grid[-1:-2:-1]:
    for term in row:
        if term >= row[y]:
            high_term.append(term)
        else:
            high_term.append(row[y])
        y += 1
        if y >= len(row):
            break
    y = 1
y = 1

old_high_term = high_term.copy()
new_high_term = []
z = 0

for row in grid[-2::-1]:
    if len(new_high_term) == 1:
        highest_sum = new_high_term
        highest_sum.append(row[0])
        highest_sum = sum(highest_sum)
        break
    else:
        new_high_term.clear()
    for term in row:
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
    old_high_term.clear()
    old_high_term = new_high_term.copy()
    y = 1
    z = 0

print (highest_sum)