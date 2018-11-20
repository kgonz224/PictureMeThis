
from PIL import Image, ImageDraw, ImageFont
import CharImg

msg = "The quick brown fox jumps over the LAZY dog. KKP"
fontSize = 25
style = 0
image = Image.open("SnowLeopard.png")
myFont = ImageFont.truetype('FreeMonoBold.ttf', fontSize) #user

(charWidth, charHeight), charImgs = CharImg.createCharacterImgs(msg, myFont)
charImgs = CharImg.styleCharImgs(charImgs, style)

charImgs[0].save("test.png", "PNG")
#character placement on Image

imgWidth, imgHeight = image.size

letter = 0
numLetters = len(charImgs)
vPos = (imgWidth % charWidth) / 2
initHPos = (imgHeight % charHeight) / 2
columns = imgWidth//charWidth
rows = imgHeight//charHeight

for r in range(0, rows):
    hPos = initHPos
    for c in range(0, columns):

        image.paste(charImgs[letter], (hPos, vPos), charImgs[letter])
        hPos = hPos + charWidth
        letter = (letter + 1) % numLetters

    vPos = vPos + charHeight

image.save('result.png')

