"""
This is a program I wrote that takes my truck drawing code from lab_02.py and turns it into a function.
I did this on my own before completing Chapter 09. Let's see how close I am to the tutorial!
"""

import arcade

def draw_truck(center_x, center_y, color):
    # Body
    truck_body = arcade.Rect(0, 0, 0, 0, 200, 40, center_x, center_y)
    arcade.draw_rect_filled(truck_body, color)
    # Cab, windshield portion
    arcade.draw_triangle_filled((center_x - 75), (center_y + 10), (center_x - 35), (center_y + 65), (center_x - 25), (center_y + 10), color)
    # Cab, main portion
    arcade.draw_lrbt_rectangle_filled((center_x - 35), (center_x + 15), (center_y + 10), (center_y + 65), color)
    # Windows
    arcade.draw_triangle_filled((center_x - 62), (center_y + 20), (center_x - 35), (center_y + 60), (center_x - 35), (center_y + 20), (0, 0, 0, 255))
    arcade.draw_lrbt_rectangle_filled((center_x - 33), center_x + 10, (center_y + 20), (center_y + 60), (0, 0, 0, 255))
    # Wheels
    arcade.draw_circle_filled((center_x - 65), (center_y - 20), 15, (0, 0, 0, 255))
    arcade.draw_circle_filled((center_x + 65), (center_y - 20), 15, (0, 0, 0, 255))

arcade.open_window(800, 600, "Drawing With Functions")
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

arcade.start_render()

draw_truck(200, 300, arcade.csscolor.DARK_GREEN)

draw_truck(600, 300, arcade.csscolor.GOLD)

arcade.finish_render()

arcade.run()