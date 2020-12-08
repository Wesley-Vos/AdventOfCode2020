def parse_bags():
    with open("input.txt") as f:
        raw_data = f.read().replace(" bags", "").replace(" bag", "").splitlines()

    data = {}
    for d in raw_data:
        outer, inner = d[:-1].split(" contain ")
        data[outer] = [[int(inner_bag[0]), inner_bag[2:]]
                       for inner_bag in inner.split(", ") if inner_bag[0] != "n"]
    return data


def find_bag(bag, bag_found, bags):
    '''Given a bag with the content, check if a bag is contained in one the bags (or the content of that bags or ...)'''
    for subbag in bag:
        if subbag[1] == bag_found or find_bag(bags[subbag[1]], bag_found, bags):
            return 1
    return 0


def find_number(outerbag, bags):
    '''Number of bags in subbags. Recursive looping through all the subbags till a subbag does not contain any other bag'''
    return sum([bag[0] + bag[0]*find_number(bag[1], bags)
                for bag in bags[outerbag]])


def main():
    bags = parse_bags()

    # Part 1
    counter = sum([find_bag(bags[bag], "shiny gold", bags) for bag in bags])
    print("Part1:", counter)

    # Part 2
    counter = find_number("shiny gold", bags)
    print("Part 2:", counter)


if __name__ == "__main__":
    main()
