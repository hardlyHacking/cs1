# system.py
# Solution for CS 1 Lab Assignment 3.
# Definition of the System class for gravity simulation.
# A System represents several Body objects.
# Based on code written by Aaron Watanabe and Devin Balkcom.

UNIVERSAL_GRAVITATIONAL_CONSTANT = 6.67384e-11 

from math import sqrt
from body import Body

class System:
    # To initialize a System, just save the body list.
    def __init__(self, body_list):
        self.body_list = body_list

    # Draw a System by drawing each body in the body list.
    def draw(self, cx, cy, pixels_per_meter):
        for body in self.body_list:
            body.draw(cx, cy, pixels_per_meter)

    # Compute the distance between bodies n1 and n2.
    def dist(self, n1, n2):
        dx = self.body_list[n2].get_x() - self.body_list[n1].get_x()
        dy = self.body_list[n2].get_y() - self.body_list[n1].get_y()
        return sqrt(dx * dx + dy * dy)
        
    # Compute the acceleration of all other bodies on body n.
    def compute_acceleration(self, n):
        total_ax = 0
        total_ay = 0
        n_x = self.body_list[n].get_x()
        n_y = self.body_list[n].get_y()
        
        for i in range(len(self.body_list)):
            if i != n:  # don't compute the acceleration of body n on itself!
                r = self.dist(i, n)
                a = UNIVERSAL_GRAVITATIONAL_CONSTANT * self.body_list[i].get_mass() / (r * r)
 
                # a is the magnitude of the acceleration.
                # Break it into its x and y components ax and ay,
                # and add them into the running sums total_ax and total_ay.
                dx = self.body_list[i].get_x() - n_x
                ax = a * dx / r
                total_ax += ax
                dy = self.body_list[i].get_y() - n_y
                ay = a * dy / r
                total_ay += ay
        
        # To return two values, use a tuple.
        return (total_ax, total_ay)

    # Compute the acceleration on each body, and use the acceleration
    # to update the velocity and then the position of each body.
    def update(self, timestep):
        for n in range(len(self.body_list)):
            (ax, ay) = self.compute_acceleration(n)
            self.body_list[n].update_velocity(ax, ay, timestep)
            self.body_list[n].update_position(timestep)
