
from PIL import Image, ImageDraw, ImageFont
import CharImg, ImgPlacement

msg = "Hello Katelyn, how are you enjoying once upon a time?"
fontSize = 25
style = 0
image = Image.open("SnowLeopard.png")
myFont = ImageFont.truetype('FreeMonoBold.ttf', fontSize) #user

(charWidth, charHeight), charImgs = CharImg.createCharacterImgs(msg, myFont)
charImgs = CharImg.styleCharImgs(charImgs, style)
final = ImgPlacement.charOnImg(charImgs, image)

final.save('result.png')

