"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Clayton Mayfield.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TOD: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.

import rosegraphics as rg

window = rg.TurtleWindow()

turtle_1 = rg.SimpleTurtle('turtle')
turtle_1.pen = rg.Pen('blue', 3)
turtle_1.speed = 8  # Fast
turtle_2 = rg.SimpleTurtle('turtle')
turtle_2.pen = rg.Pen('red', 3)
turtle_2.speed = 5  # Fast

size_1 = 50
size_2 = 200

for k in range(15):

    turtle_1.draw_circle(size_1)

    turtle_1.pen_up()
    turtle_1.forward(20)
    turtle_1.left(50)
    turtle_1.backward(25+k)
    turtle_1.pen_down()
    size_1 = size_1 - 14

    turtle_2.draw_square(size_2)

    turtle_2.pen_up()
    turtle_2.backward(50)
    turtle_2.right(45)
    turtle_2.backward(50-k)
    turtle_2.left(30)
    turtle_2.forward(100)
    turtle_2.pen_down()
    size_2 = size_2 - 14


window.close_on_mouse_click()


#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
