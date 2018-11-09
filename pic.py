from PIL import Image, ImageDraw, ImageFont

def createImg():

    msg = "The quick brown fox jumps over the LAZY dog!"
    fontSize = 10

    myFont = ImageFont.truetype('LucidaTypewriterBold.ttf', fontSize) #user


#Letter creation(Dimensions, msg, font)
    for x in msg:  # create a black and white image for each character; x => letter
        #For L: it was the only way to center the character, other options were not working properly
        mask = myFont.getmask(x)
        mask_w, mask_h = mask.size #Letter size
        W,H = mask_w + 2, mask_h + 2 #FIXME:W,H should be largest mask created Execption on space
        letter = Image.new("L", (W,H)) # grayscale image, had to draw bitmap
        d = Image.core.draw(letter.im, 0)
        d.draw_bitmap(((W - mask_w)/2, (H - mask_h)/2), mask, 255)  # 255 is pixel intensity of text
        letter.save(x+'.png')

        letter = letter.convert("RGBA")  # A is alpha channel, transparency from 0.0 (fully transparent) to 1.0
        pixels = letter.getdata()  # array of pixel data of character
        new_pixels = []  # new array for transparent character

        for p in pixels:
            if p[0] != 0 and p[1] != 0 and p[2] != 0:  # if pixel is not black
                new_pixels.append((255, 255, 255, 0))  # new pixel, white, transparent
            else:
                new_pixels.append(p)  # else, keep black pixel
        letter.putdata(new_pixels)  # copies pixel data into character
        letter.save("Transparent "+x+".png", "PNG")  # save transparent character

    background = Image.open('landscape.jpg')

    width, height = background.size

    v_position = 0
    letter_index = 0
    msg_length = len(msg)
    columns = width/W
    rows = height/H

    for r in range(0, int(round(rows))):
        h_position = 0
        for c in range(0, int(round(columns))):
            if letter_index == msg_length:
                letter_index = 0

            foreground = Image.open("Transparent "+msg[letter_index]+".png")
            background.paste(foreground, (h_position, v_position), foreground)
            h_position = h_position + W
            letter_index = letter_index + 1
        v_position = v_position + H

    background.save('result.png')


createImg()
