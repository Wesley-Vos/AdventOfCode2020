import re
from collections import defaultdict

def recurse_rule(idx, rules):
    rule = rules[idx]
    # print("Recurse", idx)
    for i, dis in enumerate(rule):
        for j, con in enumerate(dis):
            if isinstance(con, int):
                result = recurse_rule(con, rules)
                print(result)
                print("")
                rule[i][j] = result
            elif isinstance(con, str):
                rule[i][j] = con
                return rule
                
    return rules
        
def main():
    with open("input.txt") as f:
        raw_data = f.read().splitlines()
        
    rules = defaultdict()
    for i, rule in enumerate(raw_data[0:131]):
        raw_rule = rule.split(": ")
        rule = []
        for r in raw_rule[1].split(" | "):
            try:
                rule.append(list(map(int, r.split(" "))))
            except:
                rule.append(list(map(lambda x: x[1:2], r.split(" "))))
        rules[int(raw_rule[0])] = rule
    
    rules = recurse_rule(0, rules)
    # print(rules[0])
    
    
    messages = raw_data[132:]
    

if __name__ == "__main__":
    main()