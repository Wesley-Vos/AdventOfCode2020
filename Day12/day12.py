def part1(instructions):
    x = 0
    y = 0
    d = 90
    
    for ins, val in instructions:
        if ins == "F":
            if d == 90:
                x += val
            elif d == 270:
                x -= val
            elif d == 0:
                y += val
            elif d == 180:
                y -= val
        if ins == "L":
            d = (d - val + 360) % 360
        elif ins == "R":
            d = (d + val) % 360
        elif ins in ("N", "S"):
            y += val if ins == "N" else -val
        elif ins in ("E", "W"):
            x += val if ins == "E" else -val
    print(abs(x) + abs(y))


def part2(instructions):
    xway, yway = 10, 1
    x, y = 0, 0

    for ins, val in instructions:
        if ins == "F":
            x += xway*val
            y += yway*val
        if ins == "L" or ins == "R":
            val = (360 - val) % 360 if ins == "L" else val
            if val == 90:
                temp = yway
                yway = -xway
                xway = temp
            elif val == 180:
                xway = -xway
                yway = -yway
            elif val == 270:
                temp = yway
                yway = xway
                xway = -temp
        elif ins in ("N", "S"):
            yway += val if ins == "N" else -val
        elif ins in ("E", "W"):
            xway += val if ins == "E" else -val
    print(abs(x) + abs(y))
    
def main():
    with open("input.txt") as f:
        instr = [[d[0], int(d[1:])] for d in f.read().splitlines()]

    part1(instr)
    part2(instr)
    
    
if __name__ == "__main__":
    main()