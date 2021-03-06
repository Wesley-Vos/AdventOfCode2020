def change_input(val):
    if val == ".":
        return -1
    elif val == "L":
        return 0
    elif val == "#":
        return 1
    return -2


def access_grid(grid, r, c):
    # print(len(grid), len(grid[0]), r, c)
    if (0 <= r < len(grid)) and (0 <= c < len(grid[0])):
        return grid[r][c]
    else:
        return 0


def count_occupied(grid, r, c):
    above = access_grid(grid, r-1, c) == 1
    left = access_grid(grid, r, c-1) == 1
    right = access_grid(grid, r, c+1) == 1
    below = access_grid(grid, r+1, c) == 1
    up_left = access_grid(grid, r-1, c-1) == 1
    up_right = access_grid(grid, r-1, c+1) == 1
    bot_left = access_grid(grid, r+1, c-1) == 1
    bot_right = access_grid(grid, r+1, c+1) == 1

    return above + left + right + below + up_left + up_right + bot_left + bot_right

def count_occupied2(grid, r, c):
    above = access_grid(grid, r-1, c)
    i = 2
    while above == -1:
        above = access_grid(grid, r - i, c)
        i += 1
    above = (above == 1)
    
    left = access_grid(grid, r, c-1)
    i = 2
    while left == -1:
        left = access_grid(grid, r, c - i)
        i += 1
    left = (left == 1)
    
    
    right = access_grid(grid, r, c+1)
    i = 2
    while right == -1:
        right = access_grid(grid, r, c + i)
        i += 1
    right = (right == 1)
    
    below = access_grid(grid, r + 1, c)
    i = 2
    while below == -1:
        below = access_grid(grid, r + i, c)
        i += 1
    below = (below == 1)
    
    
    up_left = access_grid(grid, r-1, c-1)
    i = 2
    while up_left == -1:
        up_left = access_grid(grid, r -i, c - i)
        i += 1
    up_left = (up_left == 1)



    up_right = access_grid(grid, r-1, c+1)
    i = 2
    while up_right == -1:
        up_right = access_grid(grid, r -i, c+i)
        i += 1
    up_right = (up_right == 1)


    bot_left = access_grid(grid, r+1, c-1)
    i = 2
    while bot_left == -1:
        bot_left = access_grid(grid, r + i, c - i)
        i += 1
    bot_left = (bot_left == 1)



    bot_right = access_grid(grid, r+1, c+1)
    i = 2
    while bot_right == -1:
        bot_right = access_grid(grid, r + i, c + i)
        i += 1
    bot_right = (bot_right == 1)


    return above + left + right + below + up_left + up_right + bot_left + bot_right


def main():
    with open("input.txt") as f:
        grid = f.read().splitlines()
    for i, row in enumerate(grid):
        new_row = [c for c in row]
        new_row = list(map(change_input, new_row))
        grid[i] = new_row

    change = True
    while change:
        gridc = []
        for row in grid:
            gridc.append(row.copy())
        change = False
        for r in range(0, len(grid)):
            #print(grid[r])
            for c in range(0, len(grid[r])):
                if not grid[r][c]:
                    #print(r, c, "Empty")                          # Empty
                    #print(count_occupied(grid, r, c))
                    if count_occupied2(grid, r, c) == 0:
                        gridc[r][c] = 1
                        change = True
                elif grid[r][c] == 1:
                    # Occupied
                    #print(r, c, "Occupied")
                    if count_occupied2(grid, r, c) >= 5:
                        gridc[r][c] = 0                      # Empty the seat
                        change = True
        #change = False
        grid = gridc
        #print(change)
        for r in range(0, len(grid)):
            row = ""
            for c in range(0, len(grid[r])):
                if grid[r][c] == -1:
                    row += "."
                elif grid[r][c] == 1:
                    row += "#"
                else:
                    row += "L"
                row += " "
            #print(row)

    counter = 0
    for r in range(0, len(grid)):
        for c in range(0, len(grid[r])):
            counter += (grid[r][c] == 1)
    print(counter)


if __name__ == "__main__":
    main()
