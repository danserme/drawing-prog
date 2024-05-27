# Copyright 2022 Polina Bobrova
# this program allows user do draw by filling the cells just by clicking,
# user can pick the color or delete or save the whole drawing

w = 100
h = 100
header_h = 100
primary = "#FFF8A7"
secondary = "#086DF3"
text_size = 15
colors = ["#FF7613", "#6CD8A3", "#FD7CA7", "#086DF3", "#FFF8A7"]
filler = colors[0]
white = 255
hover = "#FDAF4C"
pressed = "#F77815"
num = 0

def setup():
    # main setup
    size(500, 700)
    background(primary)
    
    #setup for the header
    strokeWeight(1)
    stroke(secondary)
    global btns_size, btns_h
    textSize(text_size)
    btns_h = header_h / 2 - 10
    btns_size = text_size + 5
    headerLeft()
    btnsRightNormal()
    selectedColor(0)
    
    # draws the grid
    global t_w, t_h
    t_w = width / w
    t_h = height / h
    # vertical lines
    for i in range(1, t_w):
        line(h * i, header_h, h * i, height) 
    # horisontal lines
    for i in range(t_h):
        line(0, w * i + header_h, width, w * i + header_h)
    
def draw():
    rectMode(CORNER)
    mouseHover()
    
def mouseClicked():
    # if below header, it draws rects in cell, where the mouse was clicked
    global filler, num
    if mouseY > header_h:
        fill(filler)
        stroke(filler)
        numX = mouseX / w
        posX = numX * w
        numY = mouseY / h
        posY = numY * h
        rect(posX, posY, w, h)
    # clears the canvas
    elif mouseX > width - 200 and mouseX < width - 200 + 70 and mouseY > btns_h and mouseY < btns_h + btns_size:
        clear()
        setup()
        filler = colors[0]
    # to finish saving
    elif mouseX > width - 100 and mouseX < width - 100 + 70 and mouseY > btns_h and mouseY < btns_h + btns_size:
        toSave = get(0, header_h, width, height - header_h)
        name = "try_" + str(num) + ".png"
        toSave.save(name)
        num += 1
        
    else:
        # selects the filling color
        for i in range(len(colors)):
            if dist(mouseX, mouseY, 50 * i + 50, btns_h * 1.2) < text_size * 1.5:
                filler = colors[i]
                headerLeft()
                selectedColor(i)

# buttons at the right part of the header
def clearBtn(main, outline):
    stroke(outline)
    fill(main)
    rect(width - 200, btns_h, 70, btns_size)
    fill(outline)
    text("Clear", width - 200 + 18, btns_h + text_size)
    
def saveBtn(main, outline):
    stroke(outline)
    fill(main)
    rect(width - 100, btns_h, 70, btns_size)
    fill(outline)
    text("Save", width - 100 + 18, btns_h + text_size)
    
def btnsRightNormal():
    clearBtn(primary, secondary)
    saveBtn(primary, secondary)

# visual interaction for the buttons in the right part of the header
def mouseHover():
    if mouseX > width - 200 and mouseX < width - 200 + 70 and mouseY > btns_h and mouseY < btns_h + btns_size:
        if mousePressed:
            clearBtn(pressed, primary)
        else:
            clearBtn(hover, secondary)
    # to finish saving
    elif mouseX > width - 100 and mouseX < width - 100 + 70 and mouseY > btns_h and mouseY < btns_h + btns_size:
        if mousePressed:
            saveBtn(pressed, primary)
        else:
            saveBtn(hover, secondary)
    else:
         btnsRightNormal()

# color picker    
def headerLeft():
    ellipseMode(CENTER)
    for i in range(len(colors)):
        # hides all indications of previous selections
        noStroke()
        rectMode(CENTER)
        fill(primary)
        rect(50 * i + 50, btns_h * 1.2, text_size * 2.2, text_size * 2.2)
        # draws the circles with colors
        fill(colors[i])
        stroke(secondary)
        circle(50 * i + 50, btns_h * 1.2, text_size * 1.5)
        rectMode(CORNER)

# indicates the selected color        
def selectedColor(i):
    noFill()
    stroke(secondary)
    circle(50 * i + 50, btns_h * 1.2, text_size * 1.9)
    
# ----------------------------------------------------------------------
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
