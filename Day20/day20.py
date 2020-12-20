def find_adjacent(ID_f, images):
    image_f = images[ID_f]
    for ID, image in images.items():
        if ID == ID_f:
            continue
        left = True
        right = True

        for i, row in enumerate(image):
            # left
            if row[-1] != image_f[i][0]:
                left = False
            # right
            elif row[0] != image_f[i][-1]:
                right = False

        #print(image_f[0], image[-1])
        top = image_f[0] == image[-1]
        bottom = image_f[-1] == image[0]

        if left or right or top or bottom:
            print("Found adjacent", ID, left, right, top, bottom)
            break


def main():
    with open('input.txt') as f:
        raw_data = f.read()
    raw_images = [image.splitlines() for image in raw_data.split("\n\n")[0:-1]]
    images = {int(image[0][5:9]): [[c for c in row]
                                   for row in image[1:]] for image in raw_images}

    find_adjacent(3391, images)


if __name__ == "__main__":

    main()
