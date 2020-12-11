def change(val):
    if val == ".":
        return -1
    elif val == "L":
        return 0
    else:
        return 1
        
def access_grid(grid, r, c):
    if 0 <= r < len(grid):
        return grid[r][c]
    else:
        return 0
        
def count_occupied(grid, r, c):
    above = access_grid(grid, r-1, c)
    left = access_grid(grid, r, c-1)
    right = access_grid(grid, r, c+1)
    below = access_grid(grid, r+1, c)
    up_left = access_grid(grid, r-1, c-1)
    up_right = access_grid(grid, r-1, c+1)
    bot_left = access_grid(grid, r+1, c-1)
    bot_right = access_grid(grid, r+1, c+1)

def main():
    with open("input.txt") as f:
        grid = f.read().splitlines()
    for i, row in enumerate(grid):
        new_row = [c for c in row]
        new_row = list(map(change, new_row))
        grid[i] = new_row
        
    for r in grid:
        for c in r:
            if not grid[r][c]:
                
                
    
if __name__ == "__main__":
    main()
