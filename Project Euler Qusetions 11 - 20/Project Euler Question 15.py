#Project Euler Question 15

#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20×20 grid?

def grid_routes(x):
    if x == 1:
        return 2
    else:
        grid_check = grid_routes(x-1)
        return int((3 * grid_check) + (((x-2)/x) * grid_check))

print (grid_routes(20), "is the number of routes for a n by n grid")