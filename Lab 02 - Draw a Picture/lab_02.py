"""
This is a Python script that draws an image as a means of practicing using different functions and rendering
primitives on a cartesian plane.
"""

import arcade

arcade.open_window(800, 600, "Cool Truck")

arcade.set_background_color((90, 173, 250, 255))

arcade.start_render()

# Grass
arcade.draw_lrbt_rectangle_filled(0, 800, 0, 200, (33, 125, 0, 255))

# Truck
# Body
truck_body = arcade.Rect(0, 0, 0, 0, 200, 40, 150, 215)
arcade.draw_rect_filled(truck_body, (207, 0, 0, 255))
# Cab, windshield portion
arcade.draw_triangle_filled(75, 225, 115, 280, 115, 225, (207, 0, 0, 255))
# Cab, main portion
arcade.draw_lrbt_rectangle_filled(115, 165, 225, 280, (207, 0, 0, 255))
# Windows
arcade.draw_triangle_filled(88, 235, 115, 275, 115, 235, arcade.csscolor.BLACK)
arcade.draw_lrbt_rectangle_filled(117, 160, 235, 275, (0, 0, 0, 255))
# Wheels
arcade.draw_circle_filled(85, 195, 15, (0, 0, 0, 255))
arcade.draw_circle_filled(215, 195, 15, (0, 0, 0, 255))

# Garage
# Rear face of building
arcade.draw_arc_filled(750, 180, 250, 415, arcade.csscolor.GREY, 0, 180)
arcade.draw_arc_outline(750, 180, 250, 415, arcade.csscolor.BLACK, 0, 180, 4)
# Body of building
arcade.draw_lrbt_rectangle_filled(400, 750, 180, 387, arcade.csscolor.GREY)
# Front face of building
arcade.draw_arc_filled(400, 180, 250, 415, arcade.csscolor.GREY, 0, 180)
arcade.draw_arc_outline(400, 180, 250, 415, arcade.csscolor.BLACK, 0, 180, 4)
# Garage door
arcade.draw_lrbt_rectangle_filled(325, 475, 180, 325, (0, 0, 0, 255))

arcade.finish_render()

arcade.run()