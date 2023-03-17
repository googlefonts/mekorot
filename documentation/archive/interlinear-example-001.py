# drawbot.com - use drawbot-skia on Linux systems
# $ pip install git+https://github.com/typemytype/drawbot
from drawBot import *


# Constants, these are the main "settings" for the image
WIDTH = 2048
HEIGHT = 1024
MARGIN = 128
FRAMES = 1
GRID_VIEW = False  # Change this from "False" to "True" for a grid overlay


# Draws a grid
def grid():
    stroke(1, 0, 0, 0.3)
    strokeWidth(1)
    STEP_X, STEP_Y = 0, 0
    INCREMENT_X, INCREMENT_Y = MARGIN / 4, MARGIN / 4
    rect(MARGIN, MARGIN, WIDTH - (MARGIN * 2), HEIGHT - (MARGIN * 2))
    for x in range(58):
        polygon((MARGIN + STEP_X, MARGIN), (MARGIN + STEP_X, HEIGHT - MARGIN))
        STEP_X += INCREMENT_X
    for y in range(24):
        polygon((MARGIN, MARGIN + STEP_Y), (WIDTH - MARGIN, MARGIN + STEP_Y))
        STEP_Y += INCREMENT_Y
    polygon((WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
    polygon((0, HEIGHT / 2), (WIDTH, HEIGHT / 2))


# Draw the page/frame and a grid if "GRID_VIEW" is set to "True"
def draw_background():
    newPage(WIDTH, HEIGHT)
    fill(0)
    rect(-2, -2, WIDTH + 2, HEIGHT + 2)
    if GRID_VIEW:
        grid()
        pass
    else:
        pass


# Print font info
font("Mekorot[wght].ttf")
for axis, data in listFontVariations().items():
    print((axis, data))


# Draws the image
def draw_image():
    draw_background()
    fill(0.95)
    stroke(None)
    font("Mekorot[wght].ttf")

    fontSize(MARGIN * 0.6)
    fontVariations(wght=400)


    text("בָּרוּךְ אַתָּה ה אֱלֹהֵינוּ מֶלֶךְ", (MARGIN*2.4, MARGIN*5.5))
    text("הָעוֹלָם אֲשֶׁר קִדְּשָׁנוּ", (MARGIN*3.6, MARGIN*4.5))
    text("בְּמִצְוֹתָיו וְצִוָּנוּ", (MARGIN*4.85, MARGIN*3.5))
    text("לְהַדְלִיק נֵר חֲנֻכָּה", (MARGIN*4.15, MARGIN*2.5))
    #text("melekh haolam asher", (MARGIN, MARGIN*5.5))
    #text("kidshanu bmitzvotav vtzivanu", (MARGIN, MARGIN*5))
    #text("lhadlik ner Hanukkah", (MARGIN, MARGIN*4.5))


    fontSize(MARGIN * 0.45)
    fontVariations(wght=400)

    text("Barukh ata Adonai Eloheinu", (MARGIN*8.25, MARGIN*6))
    text("melekh haolam asher", (MARGIN*8.25, MARGIN*5.5))
    text("kidshanu bmitzvotav vtzivanu", (MARGIN*8.25, MARGIN*5))
    text("lhadlik ner Hanukkah", (MARGIN*8.25, MARGIN*4.5))

    text("Blessed are You, Lord our God,", (MARGIN*8.25, MARGIN*3.5))
    text("King of the universe,", (MARGIN*8.25, MARGIN*3))
    text("who has sanctified us with His", (MARGIN*8.25, MARGIN*2.5))
    text("Commandments and commanded", (MARGIN*8.25, MARGIN*2))
    text("us to kindle the Hanukkah lights.", (MARGIN*8.25, MARGIN*1.5))

# Build and save the image
if __name__ == "__main__":
    newDrawing()
    draw_image()
    saveImage("interlinear-example-001.png")
    endDrawing()
    print("DrawBot: Done :-)")
