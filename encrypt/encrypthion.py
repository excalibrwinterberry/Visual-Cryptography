from functionCalls.funtionsVC import *


# converting text to an image file which will work as our secret image

# content = "19BCE0558"
# font_path = "Library/Fonts/Supplemental/Arial Unicode.ttf"


def createSecrertMessage(content, font_path, dest):
    secretImg = createBlankImage(size)
    d1 = imageDrawFormat(secretImg)
    fnt = fontOfText(font_path, 60)
    drawText(d1, (50, 200), content, fnt)
    saveImage(secretImg, dest)


# generating random image

def generateRandomImage():
    randomImg = createBlankImage(tuple(2 * x for x in size))
    pixRand = pixelArray(randomImg)

    # format is (width, height)
    for y in range(500):
        for x in range(500):
            pixelChoice = randomPixel()
            if pixelChoice == 1:
                pixelChosen = diagpix1
            else:
                pixelChosen = diagpix2
            changePixels(pixelChosen, pixRand, x, y)
    saveImage(randomImg, "../images/random.png")


def generateRandomFromImage(source):
    randomImg = createBlankImage(tuple(2 * x for x in size))
    importedImg = getImage(source)
    importedImg = importedImg.resize((500, 500))
    # importedImg = importedImg.resize((1000, 1000))
    importedImg = ImageOps.grayscale(importedImg)
    pixRand = pixelArray(randomImg)
    pixImp = pixelArray(importedImg)
    avgPix = 0

    w, h = importedImg.size

    for y in range(500):
        for x in range(500):
            avgPix = avgPix + pixImp[x, y]
            # avgPix = avgPix + pixImp[x*2, y*2]
            # avgPix = avgPix + pixImp[x*2, y*2] + pixImp[x*2+1, y*2] + pixImp[x*2, y*2+1] + pixImp[x*2+1, y*2+1]
            # avgPix = avgPix / 4

    avgPix = avgPix / (w * h)

    # importedImg = importedImg.resize((500, 500))
    # pixImp = pixelArray(importedImg)

    for y in range(500):
        for x in range(500):
            # temp = (pixImp[x*2, y*2] + pixImp[x*2+1, y*2] + pixImp[x*2, y*2+1] + pixImp[x*2+1, y*2+1])/4
            if pixImp[x, y] > avgPix:
                pixelChosen = diagpix2
            else:
                pixelChosen = diagpix1
            changePixels(pixelChosen, pixRand, x, y)

    saveImage(randomImg, "../images/fromImage.png")


def generateFromImage1(source):
    randomImg = createBlankImage(tuple(2 * x for x in size))
    importedImg = getImage(source)
    # importedImg = importedImg.resize((500, 500))
    # importedImg = importedImg.resize((1000, 1000))
    importedImg = ImageOps.grayscale(importedImg)
    pixRand = pixelArray(randomImg)
    pixImp = pixelArray(importedImg)
    avgPix = 0

    w, h = importedImg.size

    for y in range(h):
        for x in range(w):
            avgPix = avgPix + pixImp[x, y]
            # avgPix = avgPix + pixImp[x*2, y*2]
            # avgPix = avgPix + pixImp[x*2, y*2] + pixImp[x*2+1, y*2] + pixImp[x*2, y*2+1] + pixImp[x*2+1, y*2+1]
            # avgPix = avgPix / 4

    avgPix = avgPix / (w * h)

    importedImg = importedImg.resize((1000, 1000))
    pixImp = pixelArray(importedImg)

    for y in range(500):
        for x in range(500):
            # temp = (pixImp[x*2, y*2] + pixImp[x*2+1, y*2] + pixImp[x*2, y*2+1] + pixImp[x*2+1, y*2+1])/4
            temp = (pixImp[x, y] + pixImp[999 - x, 999 - y] + pixImp[999 - x, y] + pixImp[x, 999 - y]) / 4

            if temp > avgPix:
                pixelChosen = diagpix2
            else:
                pixelChosen = diagpix1
            changePixels(pixelChosen, pixRand, x, y)

    saveImage(randomImg, "../images/fromImage.png")


def generateFromImage2(source, destination):
    randomImg = createBlankImage(tuple(2 * x for x in size))
    importedImg = getImage(source)
    importedImg = ImageOps.grayscale(importedImg)
    pixRand = pixelArray(randomImg)
    pixImp = pixelArray(importedImg)
    avgPix = 0

    w, h = importedImg.size

    if w > 1000 or h > 1000:
        importedImg = importedImg.resize((500, 500))
        pixImp = pixelArray(importedImg)
        w = 500
        h = 500

    for y in range(h):
        for x in range(w):
            avgPix = avgPix + pixImp[x, y]

    avgPix = avgPix / (w * h)

    importedImg1 = importedImg.resize((500, 500))
    pixImp1 = pixelArray(importedImg1)

    for y in range(500):
        for x in range(500):
            # temp = (pixImp[x*2, y*2] + pixImp[x*2+1, y*2] + pixImp[x*2, y*2+1] + pixImp[x*2+1, y*2+1])/4
            # temp = (pixImp[x, y] + pixImp[999-x, 999-y] + pixImp[999-x, y] + pixImp[x, 999-y])/4
            if x != 0 and y != 0:
                tempx = (((pixImp1[x, y] ** 2) / x) * y) % w
                tempy = (((pixImp1[x, y] ** 2) / y) * x) % h
            else:
                tempx = (((pixImp1[x, y] ** 2) / 13) * 7) % w
                tempy = (((pixImp1[x, y] ** 2) / 7) * 11) % h
            temp = pixImp[tempx, tempy]
            if temp > avgPix:
                pixelChosen = diagpix2
            else:
                pixelChosen = diagpix1
            changePixels(pixelChosen, pixRand, x, y)

    saveImage(randomImg, destination)


def generateFromImage3(source, destination, key):
    randomImg = createBlankImage(tuple(2 * x for x in size))
    importedImg = getImage(source)
    importedImg = ImageOps.grayscale(importedImg)
    pixRand = pixelArray(randomImg)
    pixImp = pixelArray(importedImg)
    avgPix = 0

    w, h = importedImg.size

    if w > 1000 or h > 1000:
        importedImg = importedImg.resize((500, 500))
        pixImp = pixelArray(importedImg)
        w = 500
        h = 500

    for y in range(h):
        for x in range(w):
            avgPix = avgPix + pixImp[x, y]

    avgPix = avgPix / (w * h)

    importedImg1 = importedImg.resize((500, 500))
    pixImp1 = pixelArray(importedImg1)

    for y in range(500):
        for x in range(500):
            # temp = (pixImp[x*2, y*2] + pixImp[x*2+1, y*2] + pixImp[x*2, y*2+1] + pixImp[x*2+1, y*2+1])/4
            # temp = (pixImp[x, y] + pixImp[999-x, 999-y] + pixImp[999-x, y] + pixImp[x, 999-y])/4

            x_list = genAvgPix(w, x, key)
            y_list = genAvgPix(h, y, key)

            temp = (pixImp[x_list[0], y_list[3]] + pixImp[x_list[1], y_list[2]] + pixImp[x_list[2], y_list[1]] +
                    pixImp[x_list[3], y_list[0]]) / 4

            # if x != 0 and y != 0:
            #     tempx = (((pixImp1[x,y]**2)/x)*y) % w
            #     tempy = (((pixImp1[x,y]**2)/y)*x) % h
            # else:
            #     tempx = (((pixImp1[x, y] ** 2) / 13) * 7) % w
            #     tempy = (((pixImp1[x, y] ** 2) / 7) * 11) % h
            # temp = pixImp[tempx,tempy]
            if temp > avgPix:
                pixelChosen = diagpix2
            else:
                pixelChosen = diagpix1
            changePixels(pixelChosen, pixRand, x, y)

    saveImage(randomImg, destination)


# generating cipher image

def genereateCipherImage(locationSecretImage, locationRandomImage, destination):
    randomImg = getImage(locationRandomImage)
    secretImg = getImage(locationSecretImage)
    cipherImg = createBlankImage(tuple(2 * x for x in size))

    pixCip = pixelArray(cipherImg)
    pixMsg = pixelArray(secretImg)
    pixRand = pixelArray(randomImg)

    for y in range(500):
        for x in range(500):
            if pixMsg[x, y] == 0:
                if pixRand[x * 2, y * 2] == diagpix1[0][0]:
                    pixelChosen = diagpix2
                else:
                    pixelChosen = diagpix1
            else:
                if pixRand[x * 2, y * 2] == diagpix1[0][0]:
                    pixelChosen = diagpix1
                else:
                    pixelChosen = diagpix2
            changePixels(pixelChosen, pixCip, x, y)
    saveImage(cipherImg, destination)

# generateRandomImage(size)
# generateRandomFromImage("../images/sample.jpeg", size)
# generateFromImage1("../images/sample1.jpeg")

# createSecrertMessage(content, font_path, "../images/secret.png")
# generateFromImage2("../images/sample.jpeg")
#
#
# generateFromImage3("../images/sample3.jpeg", "../images/fromImage.png", 5)
#
# genereateCipherImage("../images/secret.png", "../images/fromImage.png", "../images/cipher.png")
