#!/usr/bin/python3
import numpy as np

def power_drive(v, cw, A):
    # air density
    roh =  1.225 #kg/m**3
    return cw * A * 0.5 * v**3 * roh

def length_field(power_demand, solar, spacing):
    return power_demand/(solar * spacing)
