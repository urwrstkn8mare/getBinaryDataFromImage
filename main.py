def toBin(integer):
    return f'{integer:08b}'


def main(filename):
    from PIL import Image
    im = Image.open("in/" + filename).convert(
        mode="RGB")
    im.thumbnail((255, 255))
    height, width = im.size
    print(str(height) + ", " + str(width))
    pix = im.load()
    binary = toBin(width) + toBin(height) + toBin(24)

    totalPixels = height * width

    i = 0
    while i < height:
        ii = 0
        while ii < width:
            red, green, blue = pix[i, ii]
            binary += toBin(red) + toBin(green) + toBin(blue)
            print(str((((i*height)+ii+1) / totalPixels) * 100) + "%")
            ii += 1
        i += 1

    f = open("out/binary_" + filename + "_.txt", "w+")
    f.write(binary)
    f.close()


main('apple-splash.jpg')
