"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Brandon Wohlfarth.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()


turtle = rg.SimpleTurtle('turtle')
turtle.pen = rg.Pen('red', 1)
turtle.speed = 15

size = 200


for k in range(10):


    turtle.draw_circle(size)
    turtle.pen_up()
    turtle.right(45)
    turtle.forward(20)
    turtle.left(30)
    turtle.pen_down()
    size = size - 15

tracer = rg.SimpleTurtle()
tracer.pen = rg.Pen('green', 4)
tracer.pen_up()

tracer.forward(5)
tracer.right(90)
tracer.forward(180)
tracer.speed = 20

tracer.pen_down()
for k in range(80):
    tracer.right(15)
    tracer.forward(k)
    tracer.right(50)

window.close_on_mouse_click()