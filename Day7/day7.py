with open("input.txt") as f:
    data = f.read().splitlines()

# print(data[1])
data = [d[:-1].split(" contain ") for d in data]
data = [[d[0].split(" bags")[0], d[1].split(", ")] for d in data]
data_new = []
for d in data:
    data_add = []
    for d1 in d[1]:
        dataa = d1.replace(" bags", "").replace(" bag", "")
        if dataa[0] == "n":
            continue
        data_add.append([int(dataa[0]), dataa[2:]])

    data_new.append([d[0], data_add])

counter = 0


def find(outerbag, found_bag):
    # print(outerbag[0], "contains", outerbag[1])
    for subbag in outerbag[1]:
        # print("subbag:", subbag)
        if subbag[1] == found_bag:
            # print("Found", subbag, "in", outerbag)
            return 1
        else:
            for bag in data_new:
                if subbag[1] == bag[0]:
                    if find(bag, found_bag):
                        return 1
    return 0


counter = 0
# for bag in data_new:
#    counter += find(bag, "shiny gold")
#    #print("Counter:", counter)

# print(counter)


def find_number(outerbag):
    print("Find", outerbag)
    for bag in data_new:
        if bag[0] == outerbag:
            print("Found a bag,", bag)
            print("Subs:", bag[1])
            res = 0
            for subbag in bag[1]:

                res1 = find_number(subbag[1])
                print(res1)
                res += subbag[0] + subbag[0]*res1
            return res
    return 0


counter = find_number("shiny gold")
# for bag in data_new:
#    print(bag)
#    if bag[0] == "shiny gold":
#        for subbag in bag[1]:
#            print("Sub:", subbag)
##            counter += subbag[0]
#            counter += subbag[0]*find_number(subbag[1])

print(counter)
