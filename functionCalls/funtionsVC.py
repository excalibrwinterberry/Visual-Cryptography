from PIL import Image, ImageDraw, ImageFont
import random

size = (500, 500)

diagpix1 = [[0, 255], [255, 0]]
diagpix2 = [[255, 0], [0, 255]]


def createBlankImage(length):
    return Image.new("L", length, 255)


def imageDrawFormat(image):
    return ImageDraw.Draw(image)


def fontOfText(path, length):
    return ImageFont.truetype(path, length)


def drawText(image, cord=(0, 0), message=" ", font=None):
    image.text(cord, message, font=font, fill=0)


def pixelArray(image):
    return image.load()


def saveImage(image, location):
    image.save(location)


def randomPixel():
    return random.choice([1, 2])


def getImage(path):
    return Image.open(path)


def genAvgPix(ul, arg, key):
    a0 = ((((arg ** 2) / (9 * 17)) * 13) * key) % ul
    a1 = ((((arg ** 3) * 19) / 11) * key) % ul
    a2 = ((((arg ** 2) / 7) * 31) / key) % ul
    a3 = ((((arg * 71) / 19) ** 2) / key) % ul

    return [a0, a1, a2, a3]


def changePixels(pixSelected, pixImg, x, y):
    pixImg[x * 2, y * 2] = pixSelected[0][0]
    pixImg[x * 2 + 1, y * 2] = pixSelected[0][1]
    pixImg[x * 2, y * 2 + 1] = pixSelected[1][0]
    pixImg[x * 2 + 1, y * 2 + 1] = pixSelected[1][1]
