
from PIL import Image, ImageDraw, ImageFont
import CharImg, ImgPlacement

msg = "DRMONIQUEROSS"
fontSize = 45
#small 25 a.jpg
#medium 35 on a.jpg 
#Large 45 on a
#Make spaces transparent
#Fix border: a) test letter overflow (First letter MUST BE whole)
#            b) If disgusting center letters
#bad words
style = 2
image = Image.open("a.jpg")
myFont = ImageFont.truetype('FreeMonoBold.ttf', fontSize) #user

(charWidth, charHeight), charImgs = CharImg.createCharacterImgs(msg, myFont)
charImgs = CharImg.styleCharImgs(charImgs, style)
final = ImgPlacement.charOnImg(charImgs, image)

final.save('result.png')

image = Image.open("rainbow.jpg")
(charWidth, charHeight), charImgs = CharImg.createCharacterImgs(msg, myFont)
charImgs = CharImg.styleCharImgs(charImgs, style)
final = ImgPlacement.charOnImg(charImgs, image)
final.save('result2.png')



