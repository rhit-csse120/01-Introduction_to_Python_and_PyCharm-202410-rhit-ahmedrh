"""
An exercise that summarizes what you have learned in this Session.

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
#   Write code that accomplishes the following (and ONLY the following),
#   in the order listed:
#  _
#    - Constructs a SimpleTurtle with a  "blue"  Pen.
#    - Makes the SimpleTurtle:
#        1. Go straight UP 200 pixels.
#        2. Lift its pen UP
#             (so that the next movements do NOT leave a "trail").
#             HINT: Use the "dot trick" to figure out how to do this.
#        3. Go to the Point at (100, -40).
#             HINT: Use the "dot trick" to figure out how to do this.
#        4. Put its pen DOWN
#             (so that the next movements will return to leaving a "trail").
#        5. Have color "green" and thickness 10.
#        6. Go 150 pixels straight DOWN.
#  _
#   Don't forget to:
#     - Import rosegraphics
#     - Construct a TurtleWindow
#            [remember the required PARENTHESES for constructing an object!]
#         at the BEGINNING of your code.
#     - Ask your  TurtleWindow to   close_on_mouse_click
#          as the LAST line of your code.  (Again, parentheses needed!)
#   See the beginning and end of   m5e_loopy_turtles   for an example.
#  _
#   As always, test by running the module.
###############################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
ken = rg.SimpleTurtle()
ken.pen = rg.Pen("blue",15)
ken.left(90)
ken.forward(200)
ken.pen_up()
ken.go_to(rg.Point(100, -40))
ken.pen_down()
ken.pen.color = 'green'
ken.pen.thickness = 10
ken.left(180)
ken.forward(150)

###############################################################################
# done: 3. After you have successfully written and tested code per the above
#   (get help as needed!), be sure that you understand how to:
#     -- CONSTRUCT an INSTANCE of a CLASS (we call such instances OBJECTS).
#     -- Make an object   ** DO **   something by using a METHOD.
#     -- Reference an object's   ** DATA **   by using an INSTANCE VARIABLE.
#  _
#   If those concepts are not clear to you, ASK FOR HELP.
#   Once you understand those concepts, change the above _TODO_ to DONE.
#  _
#   As always, COMMIT-and-PUSH when you are done with this module.
###############################################################################
window.close_on_mouse_click()