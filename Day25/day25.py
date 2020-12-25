def transform_subject(val, sn):
    val *= sn
    return val%20201227
    
def transform(sn, loop):
    val = 1
    for i in range(loop):
        val = transform_subject(val, sn)
    return val
    
def find_loop_size(sn, tn):
    i = 0
    val = 1
    while(val != tn):
        val = transform_subject(val, sn)
        i += 1
    return i

def main():
    sn = 7
    
    card_pk = 5764801
    door_pk = 17807724
    card_loop = find_loop_size(sn, card_pk)
    door_loop = find_loop_size(sn, door_pk)

    ek = transform(door_pk, card_loop)
    ek2 = transform(card_pk, door_loop)
    print(ek if ek == ek2 else "Problem")
    


if __name__ == "__main__":
    main()