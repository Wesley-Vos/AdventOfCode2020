def get_neighbrs(x, y, z, w):
    # print("start")
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for dw in range(-1, 2):
                    if (dx, dy, dz, dw) != (0, 0, 0, 0): 
                        yield (x + dx, y + dy, z + dz, w + dw)

def cycle(active, w_enabled = False):
    active_new = active.copy()
    
    minx, miny, minz, minw, maxx, maxy, maxz, maxw = 10000, 10000, 10000, 10000, 0, 0, 0, 0
    
    for x, y, z, w in active:
        minx = min(minx, x)
        miny = min(miny, y)
        minz = min(minz, z)
        minw = min(minw, w)
        maxx = max(maxx, x)
        maxy = max(maxy, y)
        maxz = max(maxz, z)
        maxw = max(maxw, w)
        
        if not w_enabled:
            minw , maxw = 1, -1
            
    
    for x in range(minx - 1, maxx + 2):
        for y in range(miny - 1, maxy + 2):
            for z in range(minz - 1, maxz + 2):
                for w in range(minw - 1, maxw + 2):
                    cnt = 0
                    for cube in get_neighbrs(x, y, z, w):
                        cnt += 1*(cube in active)
                # print(x,y,z, "|", cnt)
                    if (x, y, z, w) in active:
                        if cnt != 2 and cnt != 3:
                            active_new.remove((x, y, z, w))
                    else:
                        if cnt == 3:
                           active_new.add((x, y, z, w))
    return active_new
    
    

def main():
    with open("input.txt") as f:
        data = f.read().splitlines()
        
    
    active = set()
    for y, row in enumerate(data):
        for x, cube in enumerate(row):
            if cube == "#":
                active.add((x, y, 0, 0))
    part2 = active.copy()
    for i in range(6):
        active = cycle(active)
        # if i == 1:
            #break
    print(len(active))
    
    active = part2
    for i in range(6):
        active = cycle(active, w_enabled=True)
        # if i == 1:
            #break
    print(len(active))
    
    
if __name__ == "__main__":
    main()