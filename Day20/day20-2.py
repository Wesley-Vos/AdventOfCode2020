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
        down = self._edge_to_int("".join(self.tile[-1][::-1]))
        left = self._edge_to_int("".join([row[0] for row in self.tile][::-1]))
        right = self._edge_to_int("".join([row[-1] for row in self.tile]))
        return {"l": left, "r": right, "u": up, "d": down}
        
    def flip_h(self):
        tile = self.tile[::-1]
        #self.display()
        #print(" ")
        tilee = Tile(self.id, tile)
        #tilee.display()
        return tilee
        
        
    def flip_v(self):
        tile = [row[::-1] for row in self.tile]
        return Tile(self.id, tile)
        
    def rotate(self, amt):
        n = len(self.tile)
        tile = self.tile
        for _ in range(amt):
            # print(amt)
            # self.display()
            # print("")
            tile = [[tile[n - 1 - i][j] for i in range(n)] for j in range(n)]
        tilee = Tile(self.id, tile)
        # tilee.display()
        # print("")
        return tilee
        
        
        
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
            string = ""
            for tile in row:
                string += str(tile) + " "
            print(string)
        
        
def solve(grid, i, j, all_tiles):
    for i, tiles in enumerate(all_tiles):
        for tile in tiles:
            if i == 0 and j == 0:
                grid[i][j] = tile
                new = all_tiles[0:i] + all_tiles[i+1::]
                if not solve(grid, i + 1, j + 1, new)
            elif i == 0
    


def perm(image, all_tiles):
    for r in itertools.permutations(all_tiles, len(all_tiles)):
        print(r)
            
            
    
    
    
def main():
    with open('test_input.txt') as f:
        raw_data = f.read()
    raw_images = [image.splitlines() for image in raw_data.split("\n\n")]
    
    image = Image(int(math.sqrt(len(raw_images))), len(raw_images))
    all_tiles = []
    
    for img in raw_images:
        tile = Tile(int(img[0][5:9]), [[c for c in row] for row in img[1::]])
        tiles = []
        tiles.append(tile)
        tiles.append(tile.flip_v())
        tiles.append(tile.flip_h())
        for i in range(1, 4):
            tiles.append(tile.rotate(i))
        all_tiles.append(tiles)
    print(all_tiles)
    
    
    #perm(image, all_tiles)



    


if __name__ == "__main__":

    main()
