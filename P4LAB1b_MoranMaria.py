# Maria Moran
# July 2, 2025
# P4LAB1b
#Using the turtle program, draw your initials

# Import the library
import turtle

# Create the turtle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()

# Set turtle options
pen.pensize(5)
pen.pencolor("black")
pen.shape("arrow")

screen = turtle.Screen()
screen.bgcolor("pink")
pen = turtle.Turtle()
pen.pensize(5)
pen.speed(2)

# Code to write initials
def draw_m(pen):
    pen.pensize(5)
    pen.setheading(90)       

    # Draw letter M
    pen.forward(100)         
    pen.right(135)
    pen.forward(50)          
    pen.left(90)
    pen.forward(50)          
    pen.right(135)
    pen.forward(100)         

    # Move to the right to start next letter
    pen.penup()
    pen.setheading(0)        
    pen.forward(20)
    pen.pendown()


# Draw two M's
draw_m(pen)
draw_m(pen)

# Wait for user to close window
win.mainloop()
pen.hideturtle()
screen.mainloop()
