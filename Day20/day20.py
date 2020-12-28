
def flip(image, dir):
    if dir == "h":
        new_image = image[::-1]
    elif dir == "v":
        new_image = [img[::-1] for img in image]
        
    return  new_image
    
def rotate(image):
    return rotate
    
    
    

def find_adjacent(ID_f, images):
    image_f = images[ID_f]
    out = {"l": None, "r": None, "t": None, "b": None}
    for ID, image in images.items():
        # print("Test", ID)
        if ID == ID_f:
            continue
        left = True
        right = True
        

        for i, row in enumerate(image):
            # left
            if row[-1] != image_f[i][0]:
                left = False
            # right
            if row[0] != image_f[i][-1]:
                right = False

        #print(image_f[0], image[-1])
        top = image_f[0] == image[-1]
        bottom = image_f[-1] == image[0]

        if left or right or top or bottom:
            print("Found adjacent", ID, left, right, top, bottom)
        #out[ID] = (left, right, top, bottom)
        if left:
            out["l"] = ID
        elif right:
            out["r"] = ID
        elif top:
            out["t"] = ID
        elif bottom:
            out["b"] = ID
            
            #for i in range(len(image_f)):
                #if right:
                    #print(images[ID][i][0], images[ID_f][i][-1])
                #if left:
                    #print(images[ID][i][-1], images[ID_f][i][0])
            #if top:
                #print(images[ID][-1])
                #print(images[ID_f][0])
            #if bottom:
                #print(images[ID][0])
                #print(images[ID_f][-1]
    return out
            


def main():
    with open('test_input.txt') as f:
        raw_data = f.read()
    raw_images = [image.splitlines() for image in raw_data.split("\n\n")]
    images = {int(image[0][5:9]): [[c for c in row]
                                   for row in image[1:]] for image in raw_images}

    for image in images:
        print("Image:", image)
        print(find_adjacent(image, images))


if __name__ == "__main__":

    main()
