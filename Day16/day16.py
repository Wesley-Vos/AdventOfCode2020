def main():
    with open("input.txt") as f:
        data = f.read().splitlines()
        
    fields = data[0:20]
    ticket = data[22]
    nearby = data[25:]
    fields = [field.split(": ") for field in fields]
    fields = {field[0]: field[1].split(" or ") for field in fields}
    
    for field in fields:
        for i, range in enumerate(fields[field]):
            fields[field][i] = list(map(int, range.split("-")))
    print(fields)
    
    allowed_vals = []
    for field in fields:
        for rangev in fields[field]:
            for i in range(rangev[0], rangev[1] + 1):
                allowed_vals.append(i)
                
    
    print(allowed_vals)
    
if __name__ == "__main__":
    main()