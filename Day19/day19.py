import re
from collections import defaultdict

def recurse_rule(idx, rules):
    rule = rules[idx]
    new_rules = []
    # print("Recurse", idx)
    for i, dis in enumerate(rule):
        for j, con in enumerate(dis):
            if isinstance(con, int):
                result = recurse_rule(con, rules)
                # print(result)
                #print("")
                rule[i][j] = result
            elif isinstance(con, str):
                rule[i][j] = con
                return con
        #print(rule[i])
        new_rules.append("".join(rule[i]))
    
    #string = ""
    #for rule in new_rules:
        #string += "(?:" + rule ")" + "|"
    if len(new_rules) == 1:
        return new_rules[0]
    else:
        return "(?:" + new_rules[0] + "|" + new_rules[1] + ")"
    #return "^(?:" + ")|(?:".join(new_rules) + ")$"
        
def main():
    with open("input.txt") as f:
        raw_data, messages = f.read().split("\n\n")
        raw_data = raw_data.splitlines()
        
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
    #print((rules[0][0]))
    rules[0] = recurse_rule(0, rules)
    #print(rules[0])
    print(type(rules[0]))
    
    
    ree = re.compile(r"^" + rules[0] + "$")
    print(sum(bool(ree.match(x)) for x in messages))

if __name__ == "__main__":
    main()