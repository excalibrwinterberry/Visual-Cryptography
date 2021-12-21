from functionCalls.funtionsVC import *


def generateMergedImage(locationRandomImage, locationCipherImage, dest):
    mergeImage = createBlankImage(tuple(2 * x for x in size))
    randomImage = getImage(locationRandomImage)
    cipherImage = getImage(locationCipherImage)

    pixMerge = pixelArray(mergeImage)
    pixRandom = pixelArray(randomImage)
    pixCipher = pixelArray(cipherImage)

    # for construction of original message
    # for y in range(500):
    #     for x in range(500):
    #         pix1 = [[pixRandom[x*2, y*2], pixRandom[x*2+1, y*2]],
    #                 [pixRandom[x*2, y*2+1], pixRandom[x*2+1, y*2+1]]]
    #         pix2 = [[pixCipher[x * 2, y * 2], pixCipher[x * 2 + 1, y * 2]],
    #                 [pixCipher[x * 2, y * 2 + 1], pixCipher[x * 2 + 1, y * 2 + 1]]]
    #
    #         if pix1 == pix2:
    #             pixMerge[x, y] = 255
    #         else:
    #             pixMerge[x, y] = 0

    # overlap of random and cipher images
    for y in range(1000):
        for x in range(1000):
            if pixCipher[x, y] == pixRandom[x, y]:
                pixMerge[x, y] = pixCipher[x, y]
            else:
                pixMerge[x, y] = 0

    saveImage(mergeImage, dest)


# generateMergedImage("../images/fromImage.png", "../images/cipher.png")
