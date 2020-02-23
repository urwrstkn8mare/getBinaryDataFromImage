def progressBar(percentage: float, endr=True):
    toPrint = ""
    outOfTen = int(percentage.__round__(-1) / 10)
    i = 1
    while i <= outOfTen:
        toPrint += "\u25A0"
        i += 1
    i = 1
    while i <= 10 - outOfTen:
        toPrint += "\u25A1"
        i += 1
    toPrint += " " + str(percentage.__round__(1)) + "%"
    if endr:
        print(toPrint, end="\r")
    else:
        print(toPrint)


def toBin(integer: int) -> str:
    return f"{integer:08b}"


def main(filename: str, size):
    if filename.find("\\") != -1 or filename.find("/") != -1:
        print(
            "Only input the name of the file, not the path.\nIt should be "
            'in "test/in".'
        )
        return
    from PIL import Image

    im = Image.open("test/in/" + filename).convert(mode="RGB").rotate(90)
    im.thumbnail(size)
    width, height = im.size
    pix = im.load()
    binary = toBin(width) + toBin(height) + toBin(24)

    totalPixels = height * width

    i = 0
    while i < width:
        ii = 0
        while ii < height:
            red, green, blue = pix[i, ii]
            binary += toBin(red) + toBin(green) + toBin(blue)
            endr = True
            if i == width - 1 and ii == height - 1:
                endr = False
            progressBar(
                (((i * height) + ii + 1) / totalPixels) * 100, endr
            )
            ii += 1
        i += 1

    f = open("test/out/binary_" + filename + "_.txt", "w+")
    f.write(binary)
    f.close()
    print("Total bits: " + str(binary.__len__()))
    return


main("example.png", (255, 255))
