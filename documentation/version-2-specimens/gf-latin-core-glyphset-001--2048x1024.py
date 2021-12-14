# Render with DrawBot: drawbot.com
# Use drawbot-skia on Linux systems: https://github.com/justvanrossum/drawbot-skia
# $ pip install git+https://github.com/typemytype/drawbot
from drawBot import *


# Constants, these are the main "settings" for the image
WIDTH = 2048
HEIGHT = 1024
MARGIN = 128
FRAMES = 1
GRID_VIEW = False  # Change this from "False" to "True" for a grid overlay


# Draw a grid
def grid():
    stroke(1, 0, 0, 0.3)
    strokeWidth(1)
    STEP_X, STEP_Y = 0, 0
    INCREMENT_X, INCREMENT_Y = MARGIN / 4, MARGIN / 4
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
        grid()
    else:
        pass


# Print font info
font("v2-fonts/Mekorot[wght].ttf")
for axis, data in listFontVariations().items():
    print((axis, data))


# Draws the image
def draw_image():
    draw_background()
    fill(0.95)
    stroke(None)
    font("v2-fonts/Mekorot[wght].ttf")

    fontVariations(wght=400.0)  # Range: 400.0 -> 800.0
    fontSize(MARGIN * 0.75)
    textBox(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        (MARGIN, MARGIN * 5.5, 1792, 128 + 24),
        align="center",
    )
    textBox(
        "abcdefghijklmnopqrstuvwxyz æœç",
        (MARGIN, MARGIN * 4.75, 1792, 128 + 24),
        align="center",
    )
    textBox(
        "0123456789 !¡?¿&@¼½¾ÆÇÐÞß",
        (MARGIN, MARGIN * 4, 1792, 128 + 24),
        align="center",
    )
    textBox(
        "ÀÁÂÃÄÅÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÛÜÝ",
        (MARGIN, MARGIN * 3.25, 1792, 128 + 24),
        align="center",
    )
    textBox(
        "àáâãäåèéêëìíîïðñòóôõöùúûüýÿıþŒ",
        (MARGIN, MARGIN * 2.5, 1792, 128 + 24),
        align="center",
    )
    textBox(
        "(*)[¦]{|}#$+-/<=>\^_`~¢£¤¥§¨ª«»‹›",
        (MARGIN, MARGIN * 1.75, 1792, 128 + 24),
        align="center",
    )
    textBox(
        ".,:;•…\"'‘’‚„“”−–—¬¯°±²³´µ¶·¸¹ºˆ˚˜⁄⁴€∕%Øø÷©®",
        (MARGIN, MARGIN * 1, 1792, 128 + 24),
        align="center",
    )

    fontSize(MARGIN * 0.25)
    textBox(
        "Mekorot Latin Regular Version 2.000: Google Fonts Latin Core Character Set",
        (MARGIN, MARGIN * 6, 1792, 128),
        align="center",
    )
    textBox(
        "SIL Open Font License, Version 1.1 • https://github.com/googlefonts/mekorot",
        (MARGIN, 32, 1792, 128),
        align="center",
    )


# Build and save the image
if __name__ == "__main__":
    newDrawing()
    draw_image()
    saveImage("gf-latin-core-glyphset-001--2048x1024.png")
    endDrawing()
    print("DrawBot: Done :-)")
