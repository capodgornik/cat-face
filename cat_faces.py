'''
Author: Celine Podgornik

Description:
This program uses Turtle graphics to draw a 3 by 4 grid of cat faces.
'''

import turtle, random

def randomColor():
    '''
    This function determines a random color. 
    
    Parameters: None.

    Returns: A string representing a color.
    '''
    
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 
              'B', 'C', 'D', 'E', 'F']
    color = '#'
    for i in range(6):
        color += digits[random.randrange(16)]
    
    return color 

def randomPenFillColor(rory):
    '''
    This function sets the pencolor and fillcolor of a turtle to 
    random colors.
    
    Parameters:
    rory: a turtle that draws with the pencolor and fillcolor 
    determined in this function. 
    
    Returns: None.
    '''
    
    rory.pencolor(randomColor())
    rory.fillcolor(randomColor())
    rory.begin_fill()
    
    return None 
  
def jump(inky, xNum):
    '''
    This function causes a turtle to "jump" forward the desired amount. 
    
    Parameters:
    inky: a turtle that is used when "jumping".
    xNum: an integer that determines how far the turtle "jumps".

    Returns: None.
    '''
    
    inky.penup()
    inky.forward(xNum)
    inky.pendown()
    
    return None 

def catFace(mae, size):
    '''
    This function draws the outside of the face for the catHead function.
    
    Parameters:
    mae: a turtle that is used to draw the shape.
    size: an integer that determines the size of the shape.

    Returns: None.
    '''
    
    randomPenFillColor(mae)
    mae.right(72)
    mae.forward(size)
    for i in range(4):
        mae.left(72)
        mae.forward(size)
    mae.end_fill()
        
    return None

def catEars(brie, size):
    '''
    This function draws the ears for the catHead function.
    
    Parameters:
    brie: a turtle that is used to draw the shape.
    size: an integer that determines the size of the shape.

    Returns: None.
    '''
    
    #first ear
    randomPenFillColor(brie)
    for i in range(2):
        brie.right(120)
        brie.forward(size)  
    brie.end_fill()
    
    #second ear
    randomPenFillColor(brie)
    brie.left(50)
    brie.forward(size)
    for i in range(2):
        brie.right(120)
        brie.forward(size)
    brie.end_fill()

    return None

def catEyes(alice, size):
    '''
    This function draws the eyes for the catHead function.
    
    Parameters:
    alice: a turtle that is used to draw the shape.
    size: an integer that determines the size of the shape.

    Returns: None.
    '''
    
    #first eye
    alice.backward(size)
    alice.left(33)
    alice.penup()
    alice.forward(size/2)
    alice.pendown()
    randomPenFillColor(alice)
    alice.circle(size/15)
    alice.end_fill()
    
    #second eye
    alice.penup()
    alice.forward(size*5/8)
    alice.pendown()
    randomPenFillColor(alice)
    alice.circle(size/15)
    alice.end_fill()
    
    return None

def catNose(eliza, size):
    '''
    This function draws the nose for the catHead function.
    
    Parameters:
    eliza: a turtle that is used to draw the shape.
    size: an integer that determines the size of the shape.

    Returns: None.
    '''

    eliza.right(180)
    eliza.penup()
    eliza.forward(size/2.5)
    eliza.right(90)
    eliza.forward(size/3)
    eliza.pendown()
    eliza.right(90)
    randomPenFillColor(eliza)
    for i in range(5):
        eliza.forward(size/5)
        eliza.left(120)
    eliza.end_fill()

    return None
    
def catMouth(stella, size):
    '''
    This function draws the mouth for the catHead function.
    
    Parameters:
    stella: a turtle that is used to draw the shape.
    size: an integer that determines the size of the shape.

    Returns: None.
    '''
    
    stella.right(150)
    stella.forward(size/4.5)
    stella.penup()
    stella.right(90)
    stella.forward(size/6)
    stella.right(90)
    stella.forward(size/8)
    stella.pendown()
    stella.left(180)
    stella.circle(size/6,180)
    stella.penup()
    stella.left(60)
    stella.forward(size*10/9)
    stella.pendown()
    stella.right(113)

    return None
    
def catHead(madison, size):
    '''
    This function draws a cat head.
    
    Parameters:
    madison: a turtle that is used to draw the shape.
    size: an integer that determines the size of the shape.

    Returns: None.
    '''
    
    catFace(madison, size)
    catEars(madison,size)
    catEyes(madison, size)
    catNose(madison, size)
    catMouth(madison, size)
    
    return None     
 
def drawCatRow(jon, xNum, yNum, times, size, xAdd, yAdd):
    '''
    This function calls the catHead fuction in order to draw a cat 
    head a given number of times.  
    
    Parameters:
    jon: a turtle that is used to draw the shape(s).
    xNum: the starting x coordinate for the turtle.
    yNum: the starting y coordinate for the turtle.
    times: the number of times to repeat the cat drawing.
    size: the size of the cat head.
    xAdd: how far the turtle moves horizontally between drawings.
    yAdd: how far the turtle moves vertically between drawings.

    Returns: None.
    '''
    
    for i in range(times):
        turtle.bgcolor(randomColor())
        jon.penup()
        jon.goto(xNum,yNum)
        jon.pendown()
        catHead(jon, size)
        xNum += xAdd
        yNum += yAdd  

    return None 
  
def main():
    '''
    In this program a turtle, pierre, draws a 3 by 4 grid of 12 cats, 
    calling the randomPenFillColor and randomColor functions to make 
    the colors of the cats and the background random each time a cat is 
    drawn.
    '''
    
    pierre = turtle.Turtle()
    pierre.pensize(3)
    pierre.speed(0)
    pierre.shape("turtle")
    
    size = 50
    times = 4 
    
    drawCatRow(pierre, -250, 150, times, size, 160, -10)
    drawCatRow(pierre, -200, -25, times, size, 150, 20)
    drawCatRow(pierre, -250, -150, times, size, 150, -20)
    
    #moves turtle off of the drawing
    pierre.penup()
    pierre.setheading(0)
    jump(pierre, 100)
    
    input('Press enter to end.')  #keeps the turtle graphics window open

if __name__ == '__main__':
    main()
