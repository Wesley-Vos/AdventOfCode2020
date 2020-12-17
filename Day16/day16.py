def main():
    with open("input.txt") as f:
        data = f.read().splitlines()
        
    fields = data[0:20]
    own_ticket = [int(d) for d in data[22].split(",")]
    nearby = [list(map(int, d.split(","))) for d in data[25:]]
    fields = [field.split(": ") for field in fields]
    fields = {field[0]: field[1].split(" or ") for field in fields}
    
    for field in fields:
        for i, rangev in enumerate(fields[field]):
            fields[field][i] = list(map(int, rangev.split("-")))
    
    allowed_vals = []
    for field in fields:
        # print(fields[field])
        for rangev in fields[field]:
            # print(rangev)
            for i in range(rangev[0], rangev[1] + 1):
                allowed_vals.append(i)
                
    
    # print(nearby)
    rate = 0
    for ticket in nearby:
        for val in ticket:
            rate += val*(val not in allowed_vals)
    #print(rate)
    
    
    #print(len(nearby))
    tickets = []
    for i, ticket in enumerate(nearby):
        valid = True
        for val in ticket:
            if val not in allowed_vals:
                valid = False
                break
        if valid:
            tickets.append(ticket)
            
    print(len(tickets))
    
    results = {field: [] for field in fields}
            
    for field in fields:
        rang = fields[field]
        #print("Find for", field, "range", rang)
        allowed_vals = [val for val in range(rang[0][0], rang[0][1] + 1)]
        allowed_vals += [val for val in range(rang[1][0], rang[1][1] + 1)]
        for col in range(0, len(tickets[0])):
            #print("Try column", col)
            valid = True
            for j, ticket in enumerate(tickets):
                #print("Ticket", j, ticket[col])
                if ticket[col] not in allowed_vals:
                    
                    valid = False
                    break
            if valid:
                results[field].append(col)
                #print(field, "can be column", col)
    #print(results)
    
    cnt = [0 for _ in range(0, len(tickets[0])+1)]
    #print(cnt)
    for field, cols in results.items():
        #print(len(cols))
        cnt[len(cols)] = field
    #print(cnt)
    
    result2 = {}
    used = []
    for item in cnt:
        if item == 0:
            continue
        
        for col in results[item]:
            if col not in used:
                result2[item] = col
                used.append(col)
    #print(result2)
    
    prod = 1
    for field, col in result2.items():
        if field[0:9] == "departure":
            prod *= own_ticket[col]
    print(prod)
        
    
if __name__ == "__main__":
    main()