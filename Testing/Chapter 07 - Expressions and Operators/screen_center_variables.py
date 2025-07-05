"""
This script provides an example of storing the dimensions of the screen as constants to make drawing easier.
"""

import arcade

# Constants are denoted by variable names in all caps
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

arcade.set_background_color(arcade.csscolor.WHITE)

arcade.start_render()

arcade.draw_circle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 10, arcade.csscolor.RED)

arcade.finish_render()

arcade.run()