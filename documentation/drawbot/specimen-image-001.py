# RENDER THIS DOCUMENT WITH DRAWBOT: http://www.drawbot.com
# FONTS USED: Input Mono Compressed -- https://input.djr.com
# COMPRESSED WITH: https://github.com/kornelski/pngquant
# $ brew install pngquant
# $ pngquant image.png
from drawBot import *
import math

#[W]IDTH,[H]EIGHT,[M]ARGIN,[F]RAMES
W,H,M,F = 2048,2048,128,1

# DRAWS A GRID
def grid():
    stroke(1,0,0,0.5)
    strokeWidth(1)
    rect(M, M, W-(M*2), H-(M*2))
    stpX, stpY = 0, 0
    incX, incY = M/2, M/2
    for x in range(29):
        polygon((M+stpX, M),
                (M+stpX, H-M))
        stpX += incX
    for y in range(29):
        polygon((M, M+stpY),
                (W-M, M+stpY))
        stpY += incY
    polygon( (W/2, 0), (W/2, H) )
    polygon( (0, H/2), (W, H/2) )

# REMAP INPUT RANGE TO VF AXIS RANGE
# (E.G. SINE WAVE(-1,1) to WGHT(100,900))
def remap(value, inputMin, inputMax, outputMin, outputMax):
    inputSpan  = inputMax  - inputMin   # FIND INPUT RANGE SPAN
    outputSpan = outputMax - outputMin  # FIND OUTPUT RANGE SPAN
    valueScaled = float(value - inputMin) / float(inputSpan)
    return outputMin + (valueScaled * outputSpan)

# NEW PAGE
def new_page():
    newPage(W, H)
    #frameDuration(1/24)
    fill(0)
    rect(-2, -2, W+2, H+2)

# MAIN
new_page()
font("fonts/ttf/Mekorot-Rashi-Regular.ttf")
#grid() # Toggle for grid view
fill(1)
stroke(None)
fontSize(M*1.3)
text("אבּבגדהוזחטיכּכךּך", (M*3.6, M*13))
text("למםנןסעפּפףצץ", (M*4.2, M*11.5))
text("קרשׁשׂתּת", (M*5.75, M*10))
fontSize(M*0.5)
text("abcdefghijklmnopqrstuvwxyz", (M*4.75, M*8.75))
text("ABCDEFJHIJKLMNOPQRSTUVWXYZ", (M*3.5, M*8.25))
fontSize(M*1.2)
#fontSize(M*1)
#text("װײױ", (M*11, M*9))
text("אָלֶף בֵּית בֵית גִּימֵל דָּלֶת הֵא", (M*3.2, M*6.5))
text("וָו זַיִן חֵית טֵית יוֹד כַּף כַף לָמֶד", (M*1.7, M*5))
text("מֵם נוּן סָמֶך עַיִן פֵּה פֵה צַדִי", (M*2.75, M*3.5))
text("קוֹף רֵישׁ שִׁין שִׂין תּו תָו", (M*5, M*2))
text("", (M*2.8, M*2.5))

fill(0.5)
stroke(0.5)
strokeWidth(2)
line( (M, H-M), (W-M, H-M) )
line( (M, M), (W-M, M) )
font("Input Mono Compressed")
fontSize(24)
stroke(None)

text("fonts/ttf/Mekorot-Rashi-Regular.ttf", (M, H-(M*1.25)))

text("2021", (M*14.6, H-(M*1.25)))

text("https://github.com/googlefonts/mekorot @ commit 943a57a", (M, (M*1.15)))

text("SIL OPEN FONT LICENSE Version 1.1", (M*11.71, (M*1.15)))

saveImage("documentation/drawbot/specimen-001.png")
print("Drawbot: Done :-)")
