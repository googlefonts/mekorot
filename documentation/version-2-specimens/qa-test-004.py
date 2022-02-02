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
MARGIN = 64*IMAGE_SCALE
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


    fontVariations(wght=800.0)  # Range: 400.0 -> 800.0
    fontSize(GRID_UNIT * 2.55)
    tracking(-4)
    stroke(1)
    strokeWidth(4)
    fill(None)
    text("The Design of the UNIX", (MARGIN, MARGIN + GRID_UNIT*26))
    text("Operating System", (MARGIN, MARGIN + GRID_UNIT*24))

    font("v2-fonts/Spectral-ExtraBold.ttf")
    fontVariations(wght=800.0)  # Range: 400.0 -> 800.0
    fontSize(GRID_UNIT * 2.55)
    tracking(-4)
    stroke(1)
    strokeWidth(4)
    fill(None)
    text("The Design of the UNIX", (MARGIN, MARGIN + GRID_UNIT*20))
    text("Operating System", (MARGIN, MARGIN + GRID_UNIT*18))


    fontVariations(wght=700.0)  # Range: 400.0 -> 800.0
    fontSize(GRID_UNIT * 2.55)
    tracking(-4)
    text("The Design of the UNIX", (MARGIN, MARGIN + GRID_UNIT*20))
    text("Operating System", (MARGIN, MARGIN + GRID_UNIT*18))


    fontVariations(wght=600.0)  # Range: 400.0 -> 800.0
    fontSize(GRID_UNIT * 2.55)
    tracking(-6)
    text("The Design of the UNIX", (MARGIN, MARGIN + GRID_UNIT*14))
    text("Operating System", (MARGIN, MARGIN + GRID_UNIT*12))


    fontVariations(wght=500.0)  # Range: 400.0 -> 800.0
    fontSize(GRID_UNIT * 2.55)
    tracking(-8)
    text("The Design of the UNIX", (MARGIN, MARGIN + GRID_UNIT*8))
    text("Operating System", (MARGIN, MARGIN + GRID_UNIT*6))


    fontVariations(wght=400.0)  # Range: 400.0 -> 800.0
    fontSize(GRID_UNIT * 2.55)
    tracking(-10)
    text("The Design of the UNIX", (MARGIN, MARGIN + GRID_UNIT*2))
    text("Operating System", (MARGIN, MARGIN + GRID_UNIT*0))



    #fontVariations(wght=400.0)  # Range: 400.0 -> 800.0
    #fontSize(GRID_UNIT * 0.75)
    #tracking(-1)
    ##lineHeight(128.5)
    #lineHeight(GRID_UNIT * 1)
    #hyphenation(True)
    #textBox(
    #    "Unix (trademarked as UNIX) is a family of multitasking, multiuser computer operating systems that derive from the original AT&T Unix, whose development started in 1969 at the Bell Labs research center by Ken Thompson, Dennis Ritchie, and others. Initially intended for use inside the Bell System, AT&T licensed Unix to outside parties in the late 1970s, leading to a variety of both academic and commercial Unix variants from vendors including University of California, Berkeley (BSD), Microsoft (Xenix), Sun Microsystems (SunOS/Solaris), HP/HPE (HP-UX), and IBM (AIX). In the early 1990s, AT&T sold its rights in Unix to Novell, which then sold its Unix business to the Santa Cruz Operation (SCO) in 1995.[4] The UNIX trademark passed to The Open Group, an industry consortium founded in 1996, which allows the use of the mark for certified operating systems that comply with the Single UNIX Specification (SUS). However, Novell continues to own the Unix copyrights, which the SCO Group, Inc. v. Novell, Inc. court case (2010) confirmed.",
    #    (MARGIN*1, GRID_UNIT * 2.7, (WIDTH - MARGIN * 2)/1.0 , GRID_UNIT * 18),
    #    align="left",
    #)
    ##rect(MARGIN, GRID_UNIT * 22, WIDTH - MARGIN *2, GRID_UNIT * 6.7)

    ##text("https://github.com/googlefonts/mekorot/actions/runs/1684417809", (MARGIN, MARGIN*0.75))
    #text("Text Source: Wikipedia", (MARGIN*1, MARGIN*1))

# Build and save the image
if __name__ == "__main__":
    newDrawing()
    draw_image()
    saveImage("qa-test-004.png")
    endDrawing()
    print("DrawBot: Done :-)")
