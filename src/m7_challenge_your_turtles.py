"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Yiji Zhang, Mark Hays, Derek Whitley, Vibha Alangar,
         Matt Boutell, Dave Fisher, Sriram Mohan, Mohammed Noureddine,
         Amanda Stouder, Curt Clifton, Valerie Galluzzi, their colleagues and
         Henry Ahmed.
"""
###############################################################################
# done: 1.
#   On Line 7 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# done: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#  _
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2  rg.SimpleTurtle  objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#  _
#   Don't forget that you need to import rosegraphics, construct a TurtleWindow
#   and have it close_on_mouse_click, just as in all previous modules.
#  _
#   In this CHALLENGE problem, be creative!
#   Strive for way-cool pictures!  Abstract pictures rule!
#  _
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#  _
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
window.tracer(50)
john = rg.SimpleTurtle()
kam = rg.SimpleTurtle()
jack = rg.SimpleTurtle()
halls = rg.SimpleTurtle()
john.pen = rg.Pen("blue", 1)
kam.pen = rg.Pen("red", 1)
jack.pen = rg.Pen("yellow", 1)
halls.pen = rg.Pen("green", 1)
john.pen_up()
kam.pen_up()
jack.pen_up()
halls.pen_up()
for i in range(250):
    john.go_to((rg.Point(-400, -400)))
    kam.go_to((rg.Point(400, 400)))
    jack.go_to((rg.Point(400, -400)))
    halls.go_to((rg.Point(-400, 400)))
    kam.left(180)
    jack.left(90)
    halls.right(90)
    john.pen_down()
    kam.pen_down()
    jack.pen_down()
    halls.pen_down()
    john.draw_square(i*2)
    kam.draw_square(i*2)
    jack.draw_square(i * 2)
    halls.draw_square(i * 2)
    kam.pen_up()
    john.pen_up()
    jack.pen_up()
    halls.pen_up()

window.close_on_mouse_click()
