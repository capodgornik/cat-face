import turtle, random

def catFace(madison, size):
    '''
    This function draws a cat face.
    
    Parameters:
    madison: a turtle that is used to draw the shape.
    size: an integer that determines the size of the shape.

    Returns: None.
    '''
    
    catHead(madison, size)
    catEars(madison,size)
    catEyes(madison, size)
    catNose(madison, size)
    catMouth(madison, size)
    
    return None

def catHead(mae, size):
    '''
    This function draws the head for the catFace function.
    
    Parameters:
    mae: a turtle that is used to draw the shape.
    size: an integer that determines the size of the shape.

    Returns: None.
    '''
    
    random_color(mae)
    mae.begin_fill()
    mae.right(72)
    mae.forward(size)
    for i in range(4):
        mae.left(72)
        mae.forward(size)
        
    return None

def catEars(brie, size):
    '''
    This function draws the ears for the catFace function.
    
    Parameters:
    brie: a turtle that is used to draw the shape.
    size: an integer that determines the size of the shape.

    Returns: None.
    '''
    
    #First ear:
    brie.end_fill()
    brie.backward(size)
    brie.forward(size)
    random_color(brie)
    brie.begin_fill()
    for i in range(2):
        brie.right(120)
        brie.forward(size)  
    brie.end_fill()
    #Second ear:
    random_color(brie)
    brie.begin_fill()
    brie.left(50)
    brie.forward(size)
    brie.right(120)
    brie.forward(size)
    brie.right(120)
    brie.forward(size)
    brie.backward(size)
    brie.left(120)
    brie.end_fill()

    return None

def catEyes(alice, size):
    '''
    This function draws the eyes for the catFace function.
    
    Parameters:
    alice: a turtle that is used to draw the shape.
    size: an integer that determines the size of the shape.

    Returns: None.
    '''

    alice.right(87)
    alice.penup()
    alice.forward(size/2)
    alice.pendown()
    random_color(alice)
    alice.begin_fill()
    alice.circle(size/15)
    alice.end_fill()
    alice.penup()
    alice.forward(size*5/8)
    alice.pendown()
    random_color(alice)
    alice.begin_fill()
    alice.circle(size/15)
    alice.end_fill()
    
    return None

def catNose(steven, size):
    '''
    This function draws the nose for the catFace function.
    
    Parameters:
    steven: a turtle that is used to draw the shape.
    size: an integer that determines the size of the shape.

    Returns: None.
    '''

    steven.right(180)
    steven.penup()
    steven.forward(size/2.5)
    steven.right(90)
    steven.forward(size/3)
    steven.pendown()
    steven.right(90)
    random_color(steven)
    steven.begin_fill()
    for i in range(5):
        steven.forward(size/5)
        steven.left(120)
    steven.end_fill()

    return None
    
def catMouth(stella, size):
    '''
    This function draws the mouth for the catFace function.
    
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
    
def random_color(rory):
    '''
    This function sets the pencolor and fillcolor of a turtle to random colors.
    
    Parameters:
    rory: a turtle that draws with the pencolor and fillcolor determined in this function. 
    
    Returns: None.
    '''
    
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 
              'B', 'C', 'D', 'E', 'F']
    pen = '#'
    fill = '#'
    for i in range(6):
        pen += digits[random.randrange(16)]
        fill += digits[random.randrange(16)]
    rory.pencolor(pen)
    rory.fillcolor(fill)
    
    return None
  
def random_background():
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
  
def jump(inky, x):
    '''
    This function causes a turtle to "jump" forward the desired amount. 
    
    Parameters:
    pierre: a turtle that is used when "jumping".
    x: an integer that determines how far the turtle "jumps".

    Returns: None.
    '''
    
    inky.penup()
    inky.forward(x)
    inky.pendown()
    
    return None  
 
def drawCatRow(jon, xNum, yNum, times, size, xAdd, yAdd):
    '''
    This function calls the catFace fuction in order to draw a cat 
    face a given number of times.  
    
    Parameters:
    jon: a turtle that is used to draw the shape(s).
    xNum: the starting x coordinate for the turtle.
    yNum: the starting y coordinate for the turtle.
    times: the number of times to repeat the cat drawing.
    size: the size of the cat face.
    xAdd: how far the turtle moves horizontally between drawings.
    yAdd: how far the turtle moves vertically between drawings.

    Returns: None.
    '''
    
    jon.penup()
    jon.goto(xNum, yNum)
    jon.pendown()
    
    for i in range(times):
        turtle.bgcolor(random_background())
        jon.penup()
        jon.goto(xNum,yNum)
        jon.pendown()
        catFace(jon, size)
        xNum += xAdd
        yNum += yAdd  
    
    jon.penup()

    return None 
  
def main():
    '''
    In this program a turtle, pierre, draws a 3 by 4 grid of 12 cats, 
    calling the random_color and random_background functions to make 
    the colors of the cats and the background each time a cat is drawn random.
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

    pierre.setheading(0)
    jump(pierre, 100)
    
    input('Press enter to end.')  #keeps the turtle graphics window open

if __name__ == '__main__':
    main()
