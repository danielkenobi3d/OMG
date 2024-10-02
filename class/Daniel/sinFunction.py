from operator import index
import math
import pymel.core as pm
import math
locators = []
for each in range (60):
    locators.append(pm.spaceLocator())
amplitude = 5
phase = 0# math.pi
offset = 0
samples_number = 20
resolution_a = math.pi / samples_number # this value is in degrees
resolution_x = 10 / samples_number #this value is in maya units
math.sin(math.radians(90))

for index, sample_loc in enumerate(locators):
    transform_cube, cube_creation = pm.polyCube()

    sample_loc.translateX.set(resolution_x * index)
    transform_cube.translateX.set(resolution_x * index)
    y_position = amplitude * math.sin(resolution_a * index + phase) + offset
    if math.fabs(y_position)<0.1:
        height=0.1
    else:
        height = math.fabs(y_position)
    cube_creation.height.set(height)
    sample_loc.translateY.set(y_position)
    transform_cube.translateY.set(y_position/2)