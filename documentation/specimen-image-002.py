# RENDER THIS DOCUMENT WITH DRAWBOT: http://www.drawbot.com
# FONTS USED: Input Mono Compressed -- https://input.djr.com
# COMPRESSED WITH: https://github.com/kornelski/pngquant
# $ brew install pngquant
# $ pngquant image.png
from drawBot import *

# W: WIDTH, H: HEIGHT, M: MARGIN, F: FRAMES
W,H,M,F = 2048,2048,128,1

# DRAWS A GRID
def grid():
    stroke(1,0,0,0.5)
    strokeWidth(1)
    rect(M, M, W-(M*2), H-(M*2))
    STEP_X, STEP_Y = 0, 0
    INC_X, INC_Y = M/2, M/2
    for x in range(29):
        polygon((M+STEP_X, M),
                (M+STEP_X, H-M))
        STEP_X += INC_X
    for y in range(29):
        polygon((M, M+STEP_Y),
                (W-M, M+STEP_Y))
        STEP_Y += INC_Y
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

# BLOCK 1
fontSize(M*1.50)
BLOCK_1_X = 1
BLOCK_1_Y = 12.5
text("אבגדהוזחטיכךלמםנןסעפ",    (M*(BLOCK_1_X+0.0), M*(BLOCK_1_Y-0)))
text("ףצץקרשת אּאַאָבּגּדּהּוּוֹזּ טּיּ",   (M*(BLOCK_1_X+0.1), M*(BLOCK_1_Y-2)))
text("כּךּלּמּנּסּפּףּצּקּרּשׁשׂשּׁשּׂשּתּ",       (M*(BLOCK_1_X+0.7),   M*(BLOCK_1_Y-4)))

# BLOCK 2
fontSize(M*0.75)
BLOCK_2_X = 1
BLOCK_2_Y = 7
text("""ABCDEFJHIJKLMNOPQRSTUVWXYZ""",                  (M*BLOCK_2_X, M*(BLOCK_2_Y-0)))
text("""abcdefghijklmnopqrstuvwxyz 0123456789""",       (M*BLOCK_2_X, M*(BLOCK_2_Y-1)))
text("""ÀÁÂÃÄÅÈÉÊËÌÍÎÏÑÒÓÔÕÖØÙÚÛÜÝ""",                  (M*BLOCK_2_X, M*(BLOCK_2_Y-2)))
text("""àáâãäåèéêëìíîïıñòóôõöøùúûüýÿ ÆæŒœÞþ""",         (M*BLOCK_2_X, M*(BLOCK_2_Y-3)))
text("""ßðÐÇç!?¡¿@#$%^&*€£¥¢¤¶§( ){ }[ ]|¦¼½¾©®""",     (M*BLOCK_2_X, M*(BLOCK_2_Y-4)))
text(""":;.‚„,…·'"‘’“”-•<>‹›«»+−×÷=¬±µ~ªº°¹²³⁴/_\–—""", (M*BLOCK_2_X, M*(BLOCK_2_Y-5)))
#text("`¸¨⁄∕ˆ˚˜´¯")

# INFO TEXT (MONOSPACE)
fill(1)
stroke(1)
strokeWidth(2)
line((M, H-M), (W-M, H-M))
line((M, M), (W-M, M))
stroke(None)
font("Input Mono Compressed")
fontSize(32)
text("Character Set", (M*1, H-(M*1.3)))
text("fonts/ttf/Mekorot-Rashi-Regular.ttf", (M*10.35, H-(M*1.3)))
text("https://github.com/googlefonts/mekorot @ commit aec76fa", (M, (M*1.1)))
text("SIL OPEN FONT LICENSE Version 1.1", (M*10.6, (M*1.1)))

# SAVE IMAGE
saveImage("documentation/drawbot/specimen-002.png")
print("Drawbot: Done with specimen-002.png")
