# Render with DrawBot: drawbot.com
# Use drawbot-skia on Linux systems: https://github.com/justvanrossum/drawbot-skia
# Easy install(use a virtual environment if possible):
# $ pip install git+https://github.com/typemytype/drawbot
from drawBot import *


# Constants, these are the main "settings" for the image
# Adjust multiple to change output-image resolution
IMAGE_SCALE = 4
WIDTH = 1024*IMAGE_SCALE
HEIGHT = 1024*IMAGE_SCALE
MARGIN = 128*IMAGE_SCALE
GRID_UNIT = 32*IMAGE_SCALE
FRAMES = 1
GRID_VIEW = True  # Change this from "False" to "True" for a grid overlay
GRID_VIEW = False  # Change this from "False" to "True" for a grid overlay


# Load a font and print font info
font("v2-fonts/Mekorot[wght].ttf")
for axis, data in listFontVariations().items():
    print((axis, data))


# Draw a grid
def draw_grid():
    stroke(1, 0, 0, 0.9)
    strokeWidth(1)
    STEP_X, STEP_Y = 0, 0
    INCREMENT_X, INCREMENT_Y = GRID_UNIT, GRID_UNIT
    rect(MARGIN, MARGIN, WIDTH - (MARGIN * 2), HEIGHT - (MARGIN * 2))
    for x in range(57):
        polygon((MARGIN + STEP_X, MARGIN), (MARGIN + STEP_X, HEIGHT - MARGIN))
        STEP_X += INCREMENT_X
    for y in range(29):
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
        draw_grid()
    else:
        pass


# Draws the image
def draw_image():
    draw_background()
    fill(0.95)
    stroke(None)
    font("v2-fonts/Mekorot[wght].ttf")

    #fontVariations(wght=400.0)  # Range: 400.0 -> 800.0
    #fontSize(GRID_UNIT * .5)
    #tracking(None)
    #textBox(
    #    "O Thou Who art the Lord of all names and the Maker of the heavens!  I beseech Thee by them Who are the Day-Springs of Thine invisible Essence, the Most Exalted, the All-Glorious, to make of my prayer a fire that will burn away the veils which have shut me out from Thy beauty, and a light that will lead me unto the ocean of Thy Presence.",
    #    (MARGIN, GRID_UNIT * 6, (WIDTH - MARGIN *2)/2 , GRID_UNIT * 6),
    #    align="left",
    #)
    #rect(MARGIN, GRID_UNIT * 22, WIDTH - MARGIN *2, GRID_UNIT * 6.7)

    #fontVariations(wght=800.0)  # Range: 400.0 -> 800.0
    #fontSize(GRID_UNIT * .5)
    #tracking(None)
    #textBox(
    #    "O Thou Who art the Lord of all names and the Maker of the heavens!  I beseech Thee by them Who are the Day-Springs of Thine invisible Essence, the Most Exalted, the All-Glorious, to make of my prayer a fire that will burn away the veils which have shut me out from Thy beauty, and a light that will lead me unto the ocean of Thy Presence.",
    #    (MARGIN, GRID_UNIT * 1, (WIDTH - MARGIN *2)/2 , GRID_UNIT * 6),
    #    align="left",
    #)
    #rect(MARGIN, GRID_UNIT * 22, WIDTH - MARGIN *2, GRID_UNIT * 6.7)

    font("v2-fonts/Mekorot[wght].ttf")
    fontVariations(wght=670.0)  # Range: 400.0 -> 800.0
    fontSize(GRID_UNIT * 2)
    tracking(-5)
    lineHeight(210)
    textBox(
        "The Design of the UNIX Operating System",
        (MARGIN, GRID_UNIT * 19, (WIDTH - MARGIN *2) , GRID_UNIT * 9),
        align="left",
    )
    #rect(MARGIN, GRID_UNIT * 22, WIDTH - MARGIN *2, GRID_UNIT * 6.7)

    font("v2-fonts/Spectral-Bold.ttf")
    #fontVariations(wght=700.0)  # Range: 400.0 -> 800.0
    fontSize(GRID_UNIT * 2)
    tracking(-5)
    lineHeight(210)
    textBox(
        "The Design of the UNIX Operating System",
        (MARGIN, GRID_UNIT * 14, (WIDTH - MARGIN *2) , GRID_UNIT * 9),
        align="left",
    )
    #rect(MARGIN, GRID_UNIT * 22, WIDTH - MARGIN *2, GRID_UNIT * 6.7)

    font("v2-fonts/Antwerp-Bold.woff")
    #fontVariations(wght=700.0)  # Range: 400.0 -> 800.0
    fontSize(GRID_UNIT * 2)
    tracking(-5)
    lineHeight(210)
    textBox(
        "The Design of the UNIX Operating System",
        (MARGIN, GRID_UNIT * 9, (WIDTH - MARGIN *2) , GRID_UNIT * 9),
        align="left",
    )
    #rect(MARGIN, GRID_UNIT * 22, WIDTH - MARGIN *2, GRID_UNIT * 6.7)

    font("Times New Roman Bold")
    #fontVariations(wght=700.0)  # Range: 400.0 -> 800.0
    fontSize(GRID_UNIT * 2)
    tracking(-5)
    lineHeight(210)
    textBox(
        "The Design of the UNIX Operating System",
        (MARGIN, GRID_UNIT * 4, (WIDTH - MARGIN *2) , GRID_UNIT * 9),
        align="left",
    )
    #rect(MARGIN, GRID_UNIT * 22, WIDTH - MARGIN *2, GRID_UNIT * 6.7)

# Build and save the image
if __name__ == "__main__":
    newDrawing()
    draw_image()
    saveImage("qa-test-001.png")
    endDrawing()
    print("DrawBot: Done :-)")
