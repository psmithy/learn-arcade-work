"""
This is a sample program showing graphics rendered with the Arcade library and Python.

Python modules (.py files), functions and classes should have a docstring in triple quotes like this that explains
what it is. It can be used by tools like help()

This is not the same as an inline comment, started with a #
"""

import arcade

# API call to open a window
# PEP 8 calls for parameters to be separated with a single space.
arcade.open_window(800, 600, "Drawing Example")

# Set background color (sky)
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to start drawing
arcade.start_render()

# Draw left-right-bottom-top filled rectangle (grass)
arcade.draw_lrbt_rectangle_filled(0, 800, 0, 300, arcade.csscolor.GREEN)

# Create rectangle as object and draw (tree trunk)
tree_trunk = arcade.Rect(0, 0, 0, 0, 20, 60, 100, 320)
arcade.draw_rect_filled(tree_trunk, arcade.csscolor.SIENNA)
# Draw tree top
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)

# Second tree trunk
tree_trunk2 = arcade.Rect(0, 0, 0, 0, 20, 60, 180, 320)
arcade.draw_rect_filled(tree_trunk2, arcade.csscolor.SIENNA)
# Draw second tree top as an ellipse
arcade.draw_ellipse_filled(180, 370, 60, 70, arcade.csscolor.DARK_GREEN)

# Third tree, with an arc for a top
tree_trunk3 = arcade.Rect(0, 0, 0, 0, 20, 60, 260, 320)
arcade.draw_rect_filled(tree_trunk3, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(260, 350, 60, 60, arcade.csscolor.DARK_GREEN, 0, 180)

# Fourth tree utilizing a triangle for a top
tree_trunk4 = arcade.Rect(0, 0, 0, 0, 20, 60, 340, 320)
arcade.draw_rect_filled(tree_trunk4, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(315, 310, 340, 385, 365, 310, arcade.csscolor.DARK_GREEN)

# Fifth tree with a polygon for a top
tree_trunk5 = arcade.Rect(0, 0, 0, 0, 20, 60, 420, 320)
arcade.draw_rect_filled(tree_trunk5, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((395, 310),
                            (410, 385),
                            (420, 395),
                            (430, 385),
                            (445, 310)), arcade.csscolor.DARK_GREEN)

# Draw the sun
# Starting with a circle
arcade.draw_circle_filled(550, 500, 40, arcade.csscolor.YELLOW)
# and lines for sunrays
arcade.draw_line(550, 500, 490, 500, arcade.csscolor.YELLOW, 3)
arcade.draw_line(550, 500, 505, 545, arcade.csscolor.YELLOW, 3)
arcade.draw_line(550, 500, 550, 560, arcade.csscolor.YELLOW, 3)
arcade.draw_line(550, 500, 595, 545, arcade.csscolor.YELLOW, 3)
arcade.draw_line(550, 500, 610, 500, arcade.csscolor.YELLOW, 3)
arcade.draw_line(550, 500, 595, 455, arcade.csscolor.YELLOW, 3)
arcade.draw_line(550, 500, 550, 440, arcade.csscolor.YELLOW, 3)
arcade.draw_line(550, 500, 505, 455, arcade.csscolor.YELLOW, 3)

# Draw text
arcade.draw_text("Check out my forest!", 300, 250, arcade.csscolor.BLACK, 24)

# Finish drawing
arcade.finish_render()

# Keep window open until closed by user
arcade.run()
