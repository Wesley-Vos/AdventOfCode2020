import re
from collections import defaultdict

def get_coord(line, dirs):
    x, y = 0, 0
    for move in line:
        dx, dy = dirs[move]
        x += dx
        y += dy
    return (x, y)
    
def get_neigbrs(pos, dirs):
    x, y = pos
    for dir, dp in dirs.items():
        dx, dy = dp
        yield (x + dx, y + dy)
        
def move(flipped, dirs):
    maxx, maxy = 0, 0
    minx, miny = 10000, 10000
    for x, y in flipped:
        minx = min(minx, x)
        miny = min(miny, y)
        maxx = max(maxx, x)
        maxy = max(maxy, y)
    #print(minx, miny, maxx, maxy)
    
    flipped_new = flipped.copy()
    for x, y in flipped:
        neighbrs = get_neigbrs((x, y), dirs)
        cnt = 0
        for neighbr in neighbrs:
            cnt += 1*(neighbr in flipped)
        if cnt == 0 or cnt > 2:
            flipped_new.remove((x, y))
            
    for x in range(minx - 1, maxx + 2):
        for y in range(miny - 1, maxy + 2):
            # print(x, y)
            neighbrs = get_neigbrs((x, y), dirs)
            cnt = 0
            for neighbr in neighbrs:
                cnt += 1*(neighbr in flipped)
            if cnt == 2:
                flipped_new.add((x, y))
            
    #print(len(flipped_new))
    return flipped_new
                
def main():
    with open("input.txt") as f:
        data = f.read().splitlines()

    dirs = {"w": (-2, 0), "e": (2, 0), "se": (1, -1), "sw": (-1, -1), "ne": (1, 1), "nw": (-1, 1)}
    data = map(lambda x: re.findall(r'(se|ne|e|sw|nw|w)', x), data)
    flipped = set()
    
    for row in data:
        pos = get_coord(row, dirs)
        if pos in flipped:
            flipped.remove(pos)
        else:
            flipped.add(pos)
    
    print("Part 1:", len(flipped))
    
    #print(list(get_neigbrs((0, 0), dirs)))
    for _ in range(100):
        flipped = move(flipped, dirs)
    print("Part 2:", len(flipped))
    
    
if __name__ == "__main__":
    main()