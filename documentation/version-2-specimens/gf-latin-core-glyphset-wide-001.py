# Render with DrawBot: drawbot.com
# Use drawbot-skia on Linux systems: https://github.com/justvanrossum/drawbot-skia
# Easy install(use a virtual environment if possible):
# $ pip install git+https://github.com/typemytype/drawbot
from drawBot import *


# Constants, these are the main "settings" for the image
# Adjust multiple to change output-image resolution
WIDTH = 2048*2
HEIGHT = 1024*2
MARGIN = 128*2
GRID_UNIT = 32*2
FRAMES = 1
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
    fontVariations(wght=400.0)  # Range: 400.0 -> 800.0
    fontSize(GRID_UNIT * 3)
    textBox(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        (MARGIN, GRID_UNIT * 22, WIDTH - MARGIN *2, GRID_UNIT * 4.7),
        align="center",
    )
    textBox(
        "abcdefghijklmnopqrstuvwxyz@æœç",
        (MARGIN, GRID_UNIT * 19, WIDTH - MARGIN *2, GRID_UNIT * 4.7),
        align="center",
    )
    textBox(
        "0123456789$€£¥¢¤Æ&§",
        (MARGIN, GRID_UNIT * 16, WIDTH - MARGIN *2, GRID_UNIT * 4.7),
        align="center",
    )
    textBox(
        "ÁÀÂÃÄÅÉÈÊËÍÌÎÏÑÓÒÔÕÖÚÙÛÜÝ",
        (MARGIN, GRID_UNIT * 13, WIDTH - MARGIN *2, GRID_UNIT * 4.7),
        align="center",
    )
    textBox(
        "áàâãäåéèêëíıìîïðñóòôõöúùûüýÿþŒÇÐÞß",
        (MARGIN, GRID_UNIT * 10, WIDTH - MARGIN *2, GRID_UNIT * 4.7),
        align="center",
    )
    textBox(
        "(*)[¦]{|}#+-÷=±<>^_`~¨ªº«»‹›",
        (MARGIN, GRID_UNIT * 7, WIDTH - MARGIN *2, GRID_UNIT * 4.7),
        align="center",
    )
    textBox(
        "!?¡¿.,:;•…\"'‘’‚„“”−–—¬¯´%¼½¾°¹²³⁴µ¶·Øø©®",
        (MARGIN, GRID_UNIT * 4, WIDTH - MARGIN *2, GRID_UNIT * 4.7),
        align="center",
    )
    fontSize(GRID_UNIT * 1)
    textBox(
        "Mekorot Latin Regular Version 2.000: Google Fonts Latin Core Character Set",
        (MARGIN, GRID_UNIT * 23, WIDTH - MARGIN *2, GRID_UNIT * 4.9),
        align="center",
    )
    textBox(
        "SIL Open Font License, Version 1.1 • https://github.com/googlefonts/mekorot",
        (MARGIN, GRID_UNIT * 0, WIDTH - MARGIN *2, GRID_UNIT * 4.9),
        align="center",
    )


# Build and save the image
if __name__ == "__main__":
    newDrawing()
    draw_image()
    saveImage("gf-latin-core-glyphset-001.png")
    endDrawing()
    print("DrawBot: Done :-)")
