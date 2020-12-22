import re


def find_c(r, rules_c, rules_n):
    if r in rules_c:
        return rules_c[r]
    elif r in rules_n:
        n = rules_n[r]
        option1 = [find_c(n[0], rules_c, rules_n), find_c(n[1], rules_c, rules_n)]
        option2 = [find_c(n[2], rules_c, rules_n), find_c(n[3], rules_c, rules_n)]
    else:
        print("Problem", r)
    return option1 + option2

        
def main():
    with open("input.txt") as f:
        data = f.read()
        
    rules_n = {int(d[0]): d[1:] for d in re.findall(r'(\d*): (\d*) (\d*)', data)}
    print(rules_n)

    rules_c = {int(d[0]): d[1] for d in re.findall(r'(\d*): “(.)”', data)}

    messages = data.splitlines()[132:]
    
    print(find_c(0, rules_c, rules_n))
    

if __name__ == "__main__":
    main()