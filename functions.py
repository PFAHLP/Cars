#!/usr/bin/python3
import numpy as np

def power_drive(v, cw, A):
    # air density
    roh =  1.225 #kg/m**3
    print (cw * A * 0.5 * v**2 * roh)
    return cw * A * 0.5 * v**3 * roh

def length_field(power_demand, solar, spacing, eff_prod):
    power_production =  solar * eff_prod
    return power_demand/ power_production / spacing
