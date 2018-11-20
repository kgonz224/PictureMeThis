'''
crateCharacterImgs (String msg, Font font)
createCharImgs ((int charWidth, int charHeight), mask list charImg)
createMasks (string msg, Font font)
styleCharImg (Image list charImgs, int style, *(Image img))

'''

from PIL import Image, ImageDraw, ImageFont

def createCharacterImgs(msg, font):
    ''' createCharacterImg(String msg, Font font, int Style)
        Authors: Pablo Velazquez, Kevin Gonzalez
        Version: 2.0
        Date: 11/15/2018
        Args:   msg: Message with the characters being transformed into masks.
                font: A font; results from 'ImageFont.truetype('FontName.ext',
                    fontSize)'

        return: Image list charImg, (int width, int height)
            charImg list of character images in "RGBA" form.
            height of the tallest mask
            width of the widest mask
    '''

    (charWidth, charHeight), charImgs = createMasks(msg, font)
    charImgs = createCharImg((charWidth, charHeight), charImgs)
    
    return (charWidth, charHeight), charImgs

def createCharImg ((charWidth, charHeight), charImg):
    ''' createCharImg((int charWidth, int charHeight), mask list charImg)
        Authors: Pablo Velazquez, Kevin Gonzalez
        Version: 2.0
        Date: 11/14/2018
        Args: (charWidth, charHeight) Dimensions of the every character image.
              charImg: list of character masks made from getmask(char)

        return Image list charImg
            charImg list of character images in "RGBA" form.

        Notes:  (charDimension - maskDimension) / 2 is to center the character
                        in the image.
                'RGBA' Red, Green, Blue => 0(black) to 225(white)
                        A (alpha channel) => Transparency of the pixel
                        shown as nested list pixel = [red][green][blue][alpha]
    '''

    index = 0
    for mask in charImg:
        charIcon = Image.new("L", (charWidth, charHeight))
        maskWidth, maskHeight = mask.size
        bitMap = Image.core.draw(charIcon.im, 0)
        bitMap.draw_bitmap(((charWidth - maskWidth) / 2,
                            (charHeight - maskHeight) / 2), mask, 255)
        charIcon = charIcon.convert("RGBA")
        charImg[index] = charIcon
        index += 1

    return charImg

def createMasks(msg, font):
    ''' createMasks(string msg, Font font)
        Authors: Pablo Velazquez, Kevin Gonzalez
        Version: 2.0
        Date: 11/13/2018
        Args: msg Message with the characters being transformed into masks.
              font A font; results from 'ImageFont.truetype('FontName.ext',
              fontSize)'

        return ((width, height), mask list)
            height of the tallest mask,
            width of the widest mask
            list of masks, each mask corresponding with every char in msg
                in that order.
    '''

    charWidth = 0
    charHeight = 0
    masks = []

    for char in msg:
        mask = font.getmask(char)
        masks.append(mask)
        maskWidth, maskHeight = mask.size
        if(maskWidth > charWidth):
            charWidth = maskWidth
        if(maskHeight > charHeight):
            charHeight = maskHeight

    return ((charWidth, charHeight), masks)

def styleCharImgs(charImgs, style, img = None):
    ''' styleCharImg(Image list charImgs, int style, *(Image img))
        Authors: Pablo Velazquez, Kevin Gonzalez
        Version: 2.0
        Date: 11/14/2018
        Args:   charImgs: Image list of characters.
                style: integer representing the style of the characters
                    0: Transparent letters, black background
                    1: Transparent background, black letters
                    2: Black background, letters take the average color of
                            of the background image (arg 3; img) where the
                            letter will be placed.
                img: Optional argument needed when style 2 is chosen.
                    This is the background image where the letters will be
                    placed

        return Image list charImg
            charImg list with each character image changed to the style needed

        Notes: Pixel = Pixel[0] => Red, Pixel[1] => Green, Pixel[2] => Blue
                (0 - 255), Pixel[3] => transparency (0 - 1)

                charImgs => letter is white and background is black.
    '''
    minStyle = 0
    maxStyle = 2
    styledPixels= []

    if (style == 0):
        for char in charImgs:
            styledPixels = []
            pixels = char.getdata()
            for p in pixels:
                if p[0] != 255 and p[1] != 255 and p[2] != 255:
                    styledPixels.append((0, 0, 0, 126))
                else:
                    styledPixels.append((0, 0, 0, 0))

            char.putdata(styledPixels)

    elif (style == 1):
        for char in charImgs:
            pixels = char.getdata()
            for p in pixels:
                if p[0] != 225 and p[1] != 225 and p[2] != 225:
                    p = (0, 0, 0, 1)
                else:
                    p = (p[0], p[1], p[2], 0)

            char = char.putdata(pixels)

    elif (style == 2):
        if (img == None):
            print ("This style requires the hidden parameter image. This is "
                    "the background\nimage where letters will be places.")
        else:
            print "Style not supported yet. :,("
    else:
        print "This style is not supported. Try styles {0} through {1}".format(minStyle,
                maxStyle)

    return charImgs

