import math
import copy
import itertools

class Tile:
    def __init__(self, id, tile):
        self.id = id
        self.tile = tile
        self.edges = self._calc_edges()
        
    def __str__(self):
        return str(self.id)
        
        
    def __repr__(self):
        return self.__str__()
        
    def display(self):
        for row in self.tile:
            print("".join(row))
    
    def _edge_to_int(self, edge):
        return int(edge.replace(".", "0").replace("#", "1"), 2)
        
    def _calc_edges(self):
        up = self._edge_to_int("".join(self.tile[0]))
        down = self._edge_to_int("".join(self.tile[-1]))
        left = self._edge_to_int("".join([row[0] for row in self.tile]))
        right = self._edge_to_int("".join([row[-1] for row in self.tile]))
        return {"l": left, "r": right, "u": up, "d": down}
        
    def flip_h(self):
        tile = self.tile[::-1]
        return Tile(self.id, tile)
        
    def flip_v(self):
        tile = [row[::-1] for row in self.tile]
        return Tile(self.id, tile)
        
    def rotate(self, amt):
        n = len(self.tile)
        tile = self.tile
        for _ in range(amt):
            tile = [[tile[n - 1 - i][j] for i in range(n)] for j in range(n)]
        return Tile(self.id, tile)
        
        
class Image:
    def __init__(self, n, size):
        self.n = n
        self.size = size
        self.grid = [[0 for _ in range(n)] for _ in range(n)]
        
    def add(self, tile):
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] == 0:
                    self.grid[i][j] = tile
                    return

    def display(self):
        for row in self.grid:
            print(" ".join(map(str, row)))
        
        
def solve(image, pos, all_tiles):
    n = image.n
    i, j = math.floor(pos/n), pos % n
    print("Solve for pos", pos, i, j)
    
    if pos == n*n:
        print("Solution!")
        image.display()
        product = 1
        for i in (0, n-1):
            for j in (0, n-1):
                product *= image.grid[i][j].id
        print(product)
        return 1
    
    for t, tiles in enumerate(all_tiles):
        if t == 1 and pos == 0:
            break
        for tt, tile in enumerate(tiles):
            # print("Use", tile, "option", tt)
            checkI, checkJ = True, True
            
            #Upper
            if i != 0:
                checkI = (tile.edges["u"] == image.grid[i - 1][j].edges["d"])
                
            #Left
            if j != 0:
                checkJ = (tile.edges["l"] == image.grid[i][j - 1].edges["r"])
            if checkI and checkJ:
                image.grid[i][j] = tile
                new = all_tiles[0:t] + all_tiles[t+1::]
                res = solve(image, pos + 1, new)
                if res:
                    return 1
    #print("No options left")
    return 0
    
    
def main():
    with open('input.txt') as f:
        raw_data = f.read()
    raw_images = [image.splitlines() for image in raw_data.split("\n\n")]
    
    image = Image(int(math.sqrt(len(raw_images))), len(raw_images))
    all_tiles = []
    
    for img in raw_images:
        tile = Tile(int(img[0][5:9]), [[c for c in row] for row in img[1::]])
        tiles1 = [tile]
        for i in range(1, 4):
            tiles1.append(tile.rotate(i))
        tiles = tiles1.copy()
        for tile in tiles1:
            tiles.append(tile.flip_v())
            tiles.append(tile.flip_h())
        all_tiles.append(tiles)
    
    solve(image, 0, all_tiles)


if __name__ == "__main__":

    main()
