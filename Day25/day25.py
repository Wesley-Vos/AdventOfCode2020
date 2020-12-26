def transform_subject(val, sn):
    return (val*sn)%20201227
    
def transform_n_times(sn, n):
    val = 1
    for i in range(n):
        val = transform_subject(val, sn)
    return val
    
def find_loop_size(sn, tn):
    i = 0
    val = 1
    while(val != tn):
        val = transform_subject(val, sn)
        i += 1
    return i
    
def find_ek(card_pk, door_pk):
    sn = 7
    card_loop = find_loop_size(sn, card_pk)

    return transform_n_times(door_pk, card_loop)

def main():
    card_pk = 12320657
    door_pk = 9659666
    
    print(find_ek(card_pk, door_pk))

if __name__ == "__main__":
    main()