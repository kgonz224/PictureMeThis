'''
charOnImg(Image list, Imsage)
'''

from PIL import Image

def charOnImg (charImgs, background):
    '''
    charOnImg(Image list charImgs, Image background)
    authors: Pablo Velazquez, Kevin Gonzalez
    Version: 2.0
    Date: 11/24/2018
    Args:   charImgs: Image List containing the character to put on the image
                    in order. All images are the same size.
            background: Base image where the letters will be placed on.
    
    return: Image result with chars placed on the background image.
    '''
    charWidth, charHeight = charImgs[0].size
    imgWidth, imgHeight = background.size

    letter = 0
    numLetters = len(charImgs)
    vPos = (imgWidth % charWidth) / 2
    initHPos = (imgHeight % charHeight) / 2
    columns = imgWidth//charWidth
    rows = imgHeight//charHeight

    for r in range(0, rows):

        hPos = initHPos
        for c in range(0, columns):

            background.paste(charImgs[letter], (hPos, vPos), charImgs[letter])
            hPos = hPos + charWidth
            letter = (letter + 1) % numLetters

        vPos = vPos + charHeight
    return background

