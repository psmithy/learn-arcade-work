"""
This is a sample program showing graphics rendered with the Arcade library and Python.

Python modules (.py files), functions and classes should have a docstring in triple quotes like this that explains
what it is. It can be used by tools like help()

This is not the same as an inline comment, started with a #
"""

import arcade

# API call to open a window
# PEP 8 calls for parameters to be separated with a single space.
arcade.open_window(800, 600, "Window Example")

# Set background color
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

# Finish drawing
arcade.finish_render()

# Keep window open until closed by user
arcade.run()
