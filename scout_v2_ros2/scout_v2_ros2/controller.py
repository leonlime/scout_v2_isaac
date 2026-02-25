#!/usr/bin/env python3
class Velocity_controller:
    sat_max = 0
    sat_min = 0
    kp = 0
    ki = 0
    kd = 0
    error_integral = 0
    error_prev = 0

    def __init__ (self, sat_max, sat_min, kp, ki, kd):
        self.sat_max = sat_max
        self.sat_min = sat_min
        self.kp = kp
        self.ki = ki
        self.kd = kd

    def calculate(self, time, setpoint, process):
        # set the error
        self.error = setpoint - process
        self.error_integral =+ self.error

        # calculate the output
        control_output = self.kp*self.error + self.ki*(self.error_integral)*time + self.kd*(self.error - self.error_prev)/time

        # using saturation max and min in control_output
        control_output = max(self.sat_min, min(control_output, self.sat_max))
        # set error_prev for kd
        self.error_prev = self.error

        return control_output
