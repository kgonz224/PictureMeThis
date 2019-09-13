
from PIL import Image, ImageDraw, ImageFont
import CharImg, ImgPlacement, MessageCheck, sys

# request variables
imgName = sys.argv[1]       # string i.e. "myimage.jpg"
imageStyle = sys.argv[2]    # string i.e. "2"
msg = sys.argv[3]           # string i.e. "DRMONIQUEROSS"
font = sys.argv[4]          # string i.e. "FreeMonoBold.ttf"
fontSize = sys.argv[5]      # string i.e. "45"

#test for illegal words
msg = MessageCheck.prepMsg(msg)
if(MessageCheck.illegalWords(msg)):
    print "error.png"
    sys.quit("There is an invalid word in your message. Try again ;)")

style = int(imageStyle)
image = Image.open(imgName)
myFont = ImageFont.truetype(font, CharImg.getFontSize(image, fontSize))

(charWidth, charHeight), charImgs = CharImg.createCharacterImgs(msg, myFont)
charImgs = CharImg.styleCharImgs(charImgs, style)
final = ImgPlacement.charOnImg(charImgs, image)

final.save('result.png')
print "result.png"
