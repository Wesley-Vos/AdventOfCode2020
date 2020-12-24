def main():
    with open("input.txt") as f:
        raw_data = f.read()
        
    raw_data = [d.split("(contains") for d in raw_data.splitlines()]
    data = []
    for row in raw_data:
        r = []
        r.append(row[0].split(" "))
        r.append([d.strip() for d in row[1][:-1].split(",")])
        data.append(r)
        
    
    all_ingredients = [a for d in data for a in d[0] if a != ""]
    ingredients = set(all_ingredients)
    allergens = {aller: ingredients for aller in set([a for d in data for a in d[1]])}
    for d_ingred, d_aller in data:
        for allergene in d_aller:
            # print(allergene)
            allergens[allergene] = allergens[allergene].intersection(d_ingred)
    
    
    
    ingred_aller = [ingre for i, ingredientss in allergens.items() for ingre in ingredientss]
    diff = [ing for ing in all_ingredients if ing not in ingred_aller]
    print(len(diff))
    print(allergens)
    
    
    

if __name__ == "__main__":
    main()