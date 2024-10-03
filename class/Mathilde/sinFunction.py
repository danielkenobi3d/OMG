import math

import pymel.core as pm
locators = []
for each in range (20) :
    locators.append(pm.spaceLocator())
amplitude = 5
phase = 0 #math.pi
offset = 0
samples_number = 20
resolution_a = math.pi/ 20 # value in degrees
resolution_x = 10 / samples_number #value in maya units
math.sin(math.radians(90))

for index, sample_loc in enumerate(locators) :
    sample_loc.translateX.set(resolution_x*index)
    y_position =amplitude*math.sin(resolution_a*index+phase)+offset
    sample_loc.translateY.set(y_position)