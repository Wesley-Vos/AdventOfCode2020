import re
from collections import defaultdict

        
def main():
    with open("input.txt") as f:
        data = f.read().splitlines()
        
    
    rules = defaultdict()
    for rule in data[0:131]:
        rule = rule.split(": ")
        rules[int(rule[0])] = rule[1]
    
    result = rule[0]
    if isinstance(result, int):
        result = 
    
        

    messages = data[132:]
    

if __name__ == "__main__":
    main()