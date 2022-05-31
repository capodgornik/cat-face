import turtle, random

def catFace(madison, size):
    '''
    This function draws a cats face.
    
    Parameters:
    madison: a turtle that is used to draw the shape.
    size: an integer that determines the side length of the shape.

    Returns: None.
    '''
    
    random_color(madison)
    madison.begin_fill()
    madison.right(72)
    madison.forward(size)
    for i in range(4):
        madison.left(72)
        madison.forward(size)
    madison.end_fill()
    madison.backward(size)
    madison.forward(size)
    random_color(madison)
    madison.begin_fill()
    for i in range(2):
        madison.right(120)
        madison.forward(size)  
    madison.end_fill()
    random_color(madison)
    madison.begin_fill()
    madison.left(50)
    madison.forward(size)
    madison.right(120)
    madison.forward(size)
    madison.right(120)
    madison.forward(size)
    madison.backward(size)
    madison.left(120)
    madison.end_fill()
    madison.right(87)
    madison.penup()
    madison.forward(size/2)
    madison.pendown()
    random_color(madison)
    madison.begin_fill()
    madison.circle(size/15)
    madison.end_fill()
    madison.penup()
    madison.forward(size*5/8)
    madison.pendown()
    random_color(madison)
    madison.begin_fill()
    madison.circle(size/15)
    madison.end_fill()
    madison.right(180)
    madison.penup()
    madison.forward(size/2.5)
    madison.right(90)
    madison.forward(size/3)
    madison.pendown()
    madison.right(90)
    random_color(madison)
    madison.begin_fill()
    for i in range(5):
        madison.forward(size/5)
        madison.left(120)
    madison.end_fill()
    madison.right(150)
    madison.forward(size/4.5)
    madison.penup()
    madison.right(90)
    madison.forward(size/6)
    madison.right(90)
    madison.forward(size/8)
    madison.pendown()
    madison.left(180)
    madison.circle(size/6,180)
    madison.penup()
    madison.left(60)
    madison.forward(size*10/9)
    madison.pendown()
    madison.right(113)
    
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
  
def main():
    '''
    In this program a turtle, pierre, draws 12 cats, calling the random_color and random_background functions
    to make the colors of the cats and the background each time a cat is drawn random.
    '''
    
    pierre = turtle.Turtle()
    pierre.pensize(3)
    pierre.speed(0)
    pierre.shape("turtle")
    
    x = -250
    y = 150
    size = 50
    for i in range(4):
        background = random_background()
        turtle.bgcolor(background)
        pierre.penup()
        pierre.goto(x,y)
        pierre.pendown()
        catFace(pierre, size)
        x += 150
        y -= 10
    pierre.penup()
    x = -200
    y = -25
    pierre.goto(x,y)
    pierre.pendown()
    for i in range(4):
       background = random_background()
       turtle.bgcolor(background)
       pierre.penup()
       pierre.goto(x,y)
       pierre.pendown()
       catFace(pierre, size)
       x += 150
       y += 20
    pierre.penup()
    x = -250
    y = -150
    pierre.goto(x,y)
    pierre.pendown()
    for i in range(4):
       background = random_background()
       turtle.bgcolor(background)
       pierre.penup()
       pierre.goto(x,y)
       pierre.pendown()
       catFace(pierre, size)
       x += 150
       y -= 20
    pierre.setheading(0)
    jump(pierre, 100)
    
    input('Press enter to end.')  # keeps the turtle graphics window open

main()
