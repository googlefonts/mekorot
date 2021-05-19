# RENDER THIS DOCUMENT WITH DRAWBOT: http://www.drawbot.com
from drawBot import *
import math

#[W]IDTH,[H]EIGHT,[M]ARGIN,[F]RAMES
W,H,M,F = 1024,512,64,64

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
    for y in range(13):
        polygon((M, M+stpY),
                (W-M, M+stpY))
        stpY += incY

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
text("אבּבגהוזחטיכּכךּךלמםנן", (M*2.45, M*5))
text("סעפּפףצץקרשׁשׂתּת", (M*4.45, M*3.5))
text("װײױ", (M*11.33, M*2))

#stroke(1)
#strokeWidth(2)
#line((M*2.5, H-M), (W-(M*2.5), H-M))
#line((M*2.5, M), (W-(M*2.5), M))
#font("Helvetica")
#fontSize(24)
#stroke(None)
#
#text("Mekorot-Rashi-Regular.ttf Version 2.0", (M*2.5, H-(M*1.5)))
#
#text("15.2k", (W-M*3.42, H-(M*1.5)))
#
#text("2021", (W-M*3.27, (M*1.15)))
#
#text("SIL OPEN FONT LICENSE Version 1.1", (M*2.5, (M*1.15)))

saveImage("documentation/drawbot/specimen-001.png")
print("Drawbot: Done :-)")
