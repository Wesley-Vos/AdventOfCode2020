def main():
    with open("inputs/day6.txt") as f:
        data = f.read().split("\n\n")

    counts = 0
    for group in data:
        persons = group.split("\n")
        persons = [person for person in persons if person != ""]
        # print(persons)
        count = [0 for _ in range(0, 26)]
        for person in persons:
            for letter in person:
                count[ord(letter) - ord('a')] += 1
        # print(count)
        # print(len(persons))
        for el in count:
            if(el == len(persons)):
                print("Ja", el, len(persons))
            counts += (el == len(persons))
    
    print(counts)

if __name__ == "__main__":
    main()
