# ColorfulRosettesAndSpirals.py
# Billy Ridgeway
# A spiral alternating between spirals and rosettes.

import turtle               # Imports turtle graphics.
t = turtle.Pen()            # Creates a new turtle called t.
t.speed(0)                  # Sets the speed of the pen to fast.
turtle.bgcolor("black")     # Sets the background color to black.
t.penup()                   # Starts the program with the pen in the up position.

# Ask the user for the number of sides or circles, default to 4.
sides = int(turtle.numinput("Number of sides",
                             "How many sides in your spiral?", 4, 2, 7))

# Add a list of colors.
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Our outter spiral loop for polygons and rosettes, from size 5 to 75.
for m in range(1,60):           # Sets range in the variable 'm'.
    t.width(m//25 + 1)          # Sets the pen's width to the variable 'm' divided by 25s quotient plus 1.
    t.forward(m*4)              # Moves the pen forward by the variable 'm' times 4.
    position = t.position()     # Creates a variable to record the 'x' and 'y' positions of the pen.
    heading = t.heading()       # Creates a variable to record the heading of the pen.

    # Draw a little rosette at each EVEN corner of the spiral.
    if (m % 2 == 0):                    # Divides 'm' by 2 and if there is no remainder runs this loop.
        for n in range(sides):          # Sets the variable 'n' to the number of sides entered by the user.
            t.pendown()                 # Puts the pen down to begin drawing.
            t.pencolor(colors[n%sides]) # Cycles through our list of colors by the number of sides the user selected.
            t.circle(m/4)               # Draws a circle the size of the variable 'm' divided by 4.
            t.right(360/sides -2)       # Moves the pen right by 360 degrees divided by the number of sides entered by the user minus 2.
            t.penup()                   # Puts the pen in the up position.

    # OR, draw a little spiral at each ODD corner of the spiral.
    else:                                   # If there was a remainder, then the number was an ODD number and a polygon will be drawn.
        for n in range(3,m):                # Sets the variable 'n' to the number of sides entered by the user beginning at 3.
            t.pendown()                     # Puts the pen down to write.
            t.pencolor(colors[n % sides])   # Selects the color of the pen based on the number of sides.
            t.width(m//25 + 1)              # Sets the pen's width to the variable 'm' divided by 25s quotient plus 1.
            t.forward(n*2/3)                # Moves the pen forward by the amount of the variable times 2 divided by 3.
            t.right(360/sides - 2)          # Moves the pen to the right by 360 degrees divided by the number of sides minus 2.
            t.penup()                       # Puts the pen in the up position.
    t.setpos(position)                      # Resets the pen's position to those stored in the position variable.
    t.setheading(heading)                   # Resets the heading to the heading stored in the heading variable.
    t.left(360/sides + 2)                   # Moves the pen left by 360 degrees divided by the number of sides plus 2.
            
