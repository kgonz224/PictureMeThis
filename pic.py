from PIL import Image, ImageDraw, ImageFont

msg = "The quick brown fox jumps over the LAZY dog! Meghan!!!!! <3"
fontSize = 15

myFont = ImageFont.truetype('FreeMonoBold.ttf', fontSize) #user

def createCharacter(msg, font):
    charWidth = 0
    charHeight = 0
    masks = []
#Letter creation(Dimensions, msg, font)
    for char in msg:  # create a black and white image for each character; x => letter
        mask = font.getmask(char)
        masks.append(mask)
        maskWidth, maskHeight = mask.size #Letter size
        if(maskWidth > charWidth):
            charWidth = maskWidth
        if(maskHeight > charHeight):
            charHeight = maskHeight

    #L -> Gray Scale
    charIcon = Image.new("L", (charWidth, charHeight))
    char = 0
    for mask in masks:
        charIcon = Image.new("L", (charWidth, charHeight))
        maskWidth, maskHeight = mask.size
        bitMap = Image.core.draw(charIcon.im, 0)
        bitMap.draw_bitmap(((charWidth - maskWidth) / 2, 
                            (charHeight - maskHeight) / 2), mask, 255)
        charIcon.save("test.png", "PNG")

        charIcon = charIcon.convert("RGBA")  # A is alpha channel, transparency from 0.0 (fully transparent) to 1.0
        pixels = charIcon.getdata()  # array of pixel data of character
        styledPixels = []  # new array for transparent character

        for p in pixels:
            if p[0] != 0 and p[1] != 0 and p[2] != 0:  # if pixel is not black
                styledPixels.append((255, 255, 255, 0))  # new pixel, white, transparent
            else:
                styledPixels.append(p)  # else, keep black pixel
        charIcon.putdata(styledPixels)  # copies pixel data into character
        charIcon.save(msg[char] + ".png", "PNG")  # save transparent character

        char += 1
        charIcon = charIcon.convert("L")
    return (charWidth, charHeight)

charWidth, charHeight = createCharacter(msg, myFont)

background = Image.open('SnowLeopard.png')

width, height = background.size

v_position = 0
letter_index = 0
msg_length = len(msg)
columns = width/charWidth
rows = height/charHeight

for r in range(0, int(round(rows))):
    h_position = 0
    for c in range(0, int(round(columns))):
        if letter_index == msg_length:
            letter_index = 0

        foreground = Image.open(msg[letter_index]+".png")
        background.paste(foreground, (h_position, v_position), foreground)
        h_position = h_position + charWidth
        letter_index = letter_index + 1
    v_position = v_position + charHeight

background.save('result.png')
