# Maria Moran
# July 2, 2025
# P4LAB1
# Write a program, using turtle and loops, that draws both a square and a triangle. 

# Import the library
import turtle

# Create the turtle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()

# Set turtle options
pen.pensize(5)
pen.pencolor("blue")
pen.shape("arrow")

# Code to draw shapes
for side in range(2):
    pen.forward(100)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
# While loop that executes 3 times
sides = 3

while sides > 0:
    pen.forward(100)
    pen.left(120)
    sides = sides -1

# Wait for user to close window
win.mainloop()
