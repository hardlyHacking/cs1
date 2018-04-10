# body.py
# Solution for CS 1 Lab Assignment 2.
# Definition of the Body class for gravity simulation.
# Based on code written by Aaron Watanabe and Devin Balkcom.

from cs1lib import *

class Body:
    # Initialize a Body object.
    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        self.pixel_radius = pixel_radius
        self.r = r
        self.g = g
        self.b = b

    # Return the mass of a Body object.
    def get_mass(self):
        return self.mass

    # Return the x position of a Body object.
    def get_x(self):
        return self.x
    
    # Return the y position of a Body object.
    def get_y(self):
        return self.y
    
    # Update the position of a Body object for a given timestep.
    def update_position(self, timestep):
        self.x += self.vx * timestep
        self.y += self.vy * timestep

    # Update the velocity of a Body object for a given timestep by
    # given accelerations ax in x and ay in y.
    def update_velocity(self, ax, ay, timestep):
        self.vx += ax * timestep
        self.vy += ay * timestep

    # Have a Body object draw itself.
    def draw(self, cx, cy, pixels_per_meter):
        set_fill_color(self.r, self.g, self.b)
        disable_stroke()
        enable_fill()
        draw_circle(cx + self.x * pixels_per_meter,
                    cy + self.y * pixels_per_meter,
                    self.pixel_radius)
